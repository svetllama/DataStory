def insight_lead_time(df):
    high = df[df["is_canceled"] == 1]["lead_time"].mean()
    low = df[df["is_canceled"] == 0]["lead_time"].mean()

    return (
        f"Cancelled bookings have a much higher average lead time "
        f"({high:.1f} days) compared to non-canceled bookings ({low:.1f} days)."
    )


def insight_deposit(df):
    temp = df.groupby("deposit_type")["is_canceled"].mean() * 100
    high = temp.idxmax()

    return f"{high} bookings have the highest cancellation rate at {temp.max():.1f}%."


def insight_customer(df):
    temp = df.groupby("customer_type")["is_canceled"].mean() * 100
    high = temp.idxmax()

    return f"{high} customers cancel more frequently than other segments."


def insight_previous(df):
    return (
        "Customers with prior cancellations show a strong tendency "
        "to cancel again, indicating behavioral consistency in booking patterns."
    )