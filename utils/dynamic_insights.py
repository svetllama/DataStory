def pct(x):
    return round(x * 100, 2)


def hotel_insight(df):
    g = df.groupby("hotel")["is_canceled"].mean().sort_values(ascending=False) * 100

    top = g.index[0]
    bottom = g.index[-1]

    gap = g.iloc[0] - g.iloc[-1]

    return (
        f"{top} has the highest cancellation rate at {g.iloc[0]:.1f}%, "
        f"while {bottom} has the lowest at {g.iloc[-1]:.1f}%. "
        f"This indicates a {gap:.1f} percentage point gap between hotel types."
    )


def lead_time_insight(df):
    cancel_mean = df[df["is_canceled"] == 1]["lead_time"].mean()
    non_cancel_mean = df[df["is_canceled"] == 0]["lead_time"].mean()

    return (
        f"Cancelled bookings have an average lead time of {cancel_mean:.1f} days "
        f"compared to {non_cancel_mean:.1f} days for non-canceled bookings. "
        f"This suggests longer planning horizons increase cancellation risk."
    )


def deposit_insight(df):
    g = df.groupby("deposit_type")["is_canceled"].mean().sort_values(ascending=False) * 100

    top = g.index[0]

    return (
        f"'{top}' bookings show the highest cancellation rate at {g.iloc[0]:.1f}%. "
        f"Deposit policy is a strong driver of cancellation behavior."
    )


def segment_insight(df):
    g = df.groupby("market_segment")["is_canceled"].mean().sort_values(ascending=False) * 100

    top = g.index[0]

    return (
        f"The {top} segment shows the highest cancellation rate at {g.iloc[0]:.1f}%, "
        f"indicating channel-dependent risk patterns."
    )


def revenue_insight(df):
    cancelled_revenue = df[df["is_canceled"] == 1]["revenue"].sum()
    total_revenue = df["revenue"].sum()

    share = (cancelled_revenue / total_revenue) * 100

    return (
        f"Cancelled bookings account for {share:.1f}% of total potential revenue, "
        f"highlighting significant exposure to booking uncertainty."
    )