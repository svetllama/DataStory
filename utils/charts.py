import plotly.express as px
import pandas as pd

def plot_cancellation_by_hotel(df):
    temp = df.groupby("hotel")["is_canceled"].mean().reset_index()
    temp["cancellation_rate"] = temp["is_canceled"] * 100

    fig = px.bar(
        temp,
        x="hotel",
        y="cancellation_rate",
        color="hotel",
        text_auto=".2f",
        title="Cancellation Rate by Hotel Type"
    )
    fig.update_layout(yaxis_title="Cancellation Rate (%)", showlegend=False)
    return fig


def plot_monthly_cancellation(df):
    temp = df.groupby("arrival_date_month")["is_canceled"].mean().reset_index()
    temp["cancellation_rate"] = temp["is_canceled"] * 100

    month_order = [
        "January","February","March","April","May","June",
        "July","August","September","October","November","December"
    ]
    temp["arrival_date_month"] = pd.Categorical(
        temp["arrival_date_month"], categories=month_order, ordered=True
    )
    temp = temp.sort_values("arrival_date_month")

    fig = px.line(
        temp,
        x="arrival_date_month",
        y="cancellation_rate",
        markers=True,
        title="Monthly Cancellation Trend"
    )
    fig.update_layout(yaxis_title="Cancellation Rate (%)")
    return fig


def plot_market_segment(df):
    temp = df.groupby("market_segment")["is_canceled"].mean().reset_index()
    temp["cancellation_rate"] = temp["is_canceled"] * 100

    fig = px.bar(
        temp.sort_values("cancellation_rate", ascending=False),
        x="market_segment",
        y="cancellation_rate",
        color="market_segment",
        title="Cancellation Rate by Market Segment"
    )
    fig.update_layout(showlegend=False)
    return fig