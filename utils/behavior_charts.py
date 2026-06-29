import plotly.express as px

def plot_lead_time(df):
    fig = px.histogram(
        df,
        x="lead_time",
        color="is_canceled",
        barmode="overlay",
        nbins=50,
        title="Lead Time Distribution vs Cancellation"
    )
    fig.update_layout(xaxis_title="Lead Time (days)", yaxis_title="Count")
    return fig


def plot_deposit_type(df):
    temp = df.groupby("deposit_type")["is_canceled"].mean().reset_index()
    temp["cancellation_rate"] = temp["is_canceled"] * 100

    fig = px.bar(
        temp.sort_values("cancellation_rate", ascending=False),
        x="deposit_type",
        y="cancellation_rate",
        color="deposit_type",
        title="Cancellation Rate by Deposit Type"
    )
    fig.update_layout(yaxis_title="Cancellation Rate (%)", showlegend=False)
    return fig


def plot_customer_type(df):
    temp = df.groupby("customer_type")["is_canceled"].mean().reset_index()
    temp["cancellation_rate"] = temp["is_canceled"] * 100

    fig = px.bar(
        temp,
        x="customer_type",
        y="cancellation_rate",
        color="customer_type",
        title="Cancellation Rate by Customer Type"
    )
    fig.update_layout(yaxis_title="Cancellation Rate (%)", showlegend=False)
    return fig


def plot_previous_cancellations(df):
    temp = df.groupby("previous_cancellations")["is_canceled"].mean().reset_index()

    fig = px.line(
        temp,
        x="previous_cancellations",
        y="is_canceled",
        markers=True,
        title="Effect of Previous Cancellations on Current Cancellation Rate"
    )
    fig.update_layout(yaxis_title="Cancellation Rate")
    return fig