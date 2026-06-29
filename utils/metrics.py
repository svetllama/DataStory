def calculate_kpis(df):
    total_bookings = len(df)
    cancelled = df['is_canceled'].sum()
    cancellation_rate = (cancelled / total_bookings) * 100 if total_bookings > 0 else 0

    avg_adr = df['adr'].mean()
    avg_lead_time = df['lead_time'].mean()

    potential_revenue_loss = df[df['is_canceled'] == 1]['revenue'].sum()

    return {
        "total_bookings": total_bookings,
        "cancelled": cancelled,
        "cancellation_rate": cancellation_rate,
        "avg_adr": avg_adr,
        "avg_lead_time": avg_lead_time,
        "revenue_loss": potential_revenue_loss
    }