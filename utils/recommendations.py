def generate_recommendations(df):
    recs = []

    # Lead time insight
    avg_lead_cancel = df[df["is_canceled"] == 1]["lead_time"].mean()
    avg_lead_not = df[df["is_canceled"] == 0]["lead_time"].mean()

    if avg_lead_cancel > avg_lead_not:
        recs.append(
            "📌 Introduce reminder emails and flexible modification options for bookings with long lead times (>100 days)."
        )

    # Deposit type
    deposit_cancel = df.groupby("deposit_type")["is_canceled"].mean()
    high_dep = deposit_cancel.idxmax()

    recs.append(
        f"📌 Review cancellation policy for '{high_dep}' bookings — they show the highest cancellation tendency."
    )

    # Market segment
    segment_cancel = df.groupby("market_segment")["is_canceled"].mean()
    top_segment = segment_cancel.idxmax()

    recs.append(
        f"📌 Prioritize stricter booking confirmation or deposit rules for '{top_segment}' segment."
    )

    # Customer type
    cust_cancel = df.groupby("customer_type")["is_canceled"].mean()
    top_customer = cust_cancel.idxmax()

    recs.append(
        f"📌 Design loyalty programs targeting '{top_customer}' customers to reduce cancellation probability."
    )

    return recs


def high_risk_persona(df):
    conditions = []

    if df["lead_time"].mean() > 100:
        conditions.append("High lead time bookings")
    if "No Deposit" in df["deposit_type"].values:
        conditions.append("No deposit bookings are present")
    if df["is_repeated_guest"].mean() < 0.2:
        conditions.append("Mostly first-time guests")
    if df["market_segment"].value_counts().idxmax():
        conditions.append(f"High exposure to {df['market_segment'].value_counts().idxmax()} segment")

    return conditions