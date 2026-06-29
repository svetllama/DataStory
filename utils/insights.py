def insight_hotel(df):
    temp = df.groupby("hotel")["is_canceled"].mean() * 100
    high = temp.idxmax()
    return f"{high} shows the highest cancellation rate at {temp.max():.1f}%."


def insight_month(df):
    temp = df.groupby("arrival_date_month")["is_canceled"].mean() * 100
    high = temp.idxmax()
    return f"{high} has the highest cancellation rate across months."


def insight_market(df):
    temp = df.groupby("market_segment")["is_canceled"].mean() * 100
    high = temp.idxmax()
    return f"{high} segment shows the highest cancellations at {temp.max():.1f}%."