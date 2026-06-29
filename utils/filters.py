import streamlit as st

def apply_filters(df):
    st.sidebar.header("🔍 Filters")

    hotel = st.sidebar.multiselect(
        "Hotel Type",
        options=df['hotel'].unique(),
        default=df['hotel'].unique()
    )

    market_segment = st.sidebar.multiselect(
        "Market Segment",
        options=df['market_segment'].unique(),
        default=df['market_segment'].unique()
    )

    customer_type = st.sidebar.multiselect(
        "Customer Type",
        options=df['customer_type'].unique(),
        default=df['customer_type'].unique()
    )

    deposit_type = st.sidebar.multiselect(
        "Deposit Type",
        options=df['deposit_type'].unique(),
        default=df['deposit_type'].unique()
    )

    year = st.sidebar.multiselect(
        "Arrival Year",
        options=sorted(df['arrival_date_year'].unique()),
        default=sorted(df['arrival_date_year'].unique())
    )

    filtered_df = df[
        (df['hotel'].isin(hotel)) &
        (df['market_segment'].isin(market_segment)) &
        (df['customer_type'].isin(customer_type)) &
        (df['deposit_type'].isin(deposit_type)) &
        (df['arrival_date_year'].isin(year))
    ]

    return filtered_df