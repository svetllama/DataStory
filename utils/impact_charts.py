import plotly.express as px

def plot_adr_by_cancellation(df):
    temp = df.groupby("is_canceled")["adr"].mean().reset_index()

    temp["status"] = temp["is_canceled"].map({
        0: "Not Canceled",
        1: "Canceled"
    })

    fig = px.bar(
        temp,
        x="status",
        y="adr",
        color="status",
        title="Average Daily Rate (ADR) vs Cancellation Status"
    )
    fig.update_layout(showlegend=False, yaxis_title="Average ADR")
    return fig


def plot_revenue_risk_by_hotel(df):
    temp = df[df["is_canceled"] == 1].groupby("hotel")["revenue"].sum().reset_index()

    fig = px.bar(
        temp,
        x="hotel",
        y="revenue",
        color="hotel",
        # title="Potential Revenue at Risk by Hotel Type"
        title = "Potential Revenue Associated with Canceled Bookings"
    )
    fig.update_layout(showlegend=False, yaxis_title="Revenue at Risk")
    return fig


def plot_segment_heatmap(df):
    temp = df.groupby(["hotel", "market_segment"])["is_canceled"].mean().reset_index()

    temp["cancellation_rate"] = temp["is_canceled"] * 100

    fig = px.density_heatmap(
        temp,
        x="market_segment",
        y="hotel",
        z="cancellation_rate",
        color_continuous_scale="Reds",
        title="Cancellation Risk Heatmap: Hotel vs Market Segment"
    )

    return fig