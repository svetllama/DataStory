import streamlit as st
import plotly.express as px

from utils.ui import apply_ui
apply_ui()

from config import APP_TITLE, APP_SUBTITLE
from utils.data_loader import load_data
from utils.filters import apply_filters
from utils.metrics import calculate_kpis
from utils.styles import apply_styles

from utils.charts import (
    plot_cancellation_by_hotel,
    plot_monthly_cancellation,
    plot_market_segment
)

from utils.dynamic_insights import (
    hotel_insight,
    lead_time_insight,
    deposit_insight,
    segment_insight,
    revenue_insight
)

from utils.insights import (
    insight_hotel,
    insight_month,
    insight_market
)

from utils.behavior_charts import (
    plot_lead_time,
    plot_deposit_type,
    plot_customer_type,
    plot_previous_cancellations
)

from utils.behavior_insights import (
    insight_lead_time,
    insight_deposit,
    insight_customer,
    insight_previous
)

from utils.impact_charts import (
    plot_adr_by_cancellation,
    plot_revenue_risk_by_hotel,
    plot_segment_heatmap
)

from utils.recommendations import generate_recommendations, high_risk_persona

# ----------------------------
# PAGE CONFIG
# ----------------------------
st.set_page_config(
    page_title=APP_TITLE,
    layout="wide"
)

apply_styles()

# ----------------------------
# HEADER
# ----------------------------
st.title(APP_TITLE)
st.subheader(APP_SUBTITLE)

# ----------------------------
# LOAD DATA
# ----------------------------
DATA_PATH = "input_data/hotel_booking_data_cleaned.csv"
df = load_data(DATA_PATH)

# ----------------------------
# FILTERS
# ----------------------------
filtered_df = apply_filters(df)

# ----------------------------
# KPIS
# ----------------------------
kpis = calculate_kpis(filtered_df)

from utils.ui import section_title

# st.markdown("## 🧾 Executive Summary")
section_title("Executive Summary")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Bookings", kpis["total_bookings"])
col2.metric("Cancellation Rate", f"{kpis['cancellation_rate']:.2f}%")
col3.metric("Avg ADR", f"{kpis['avg_adr']:.2f}")
col4.metric(
    "Revenue at Risk",
    f"{kpis['revenue_loss']:.0f}"
)

st.markdown("---")

st.markdown("### 🎯 Key Insights")

st.info(
    """
- Cancellations are driven primarily by long lead times and no-deposit bookings
- City Hotels show higher cancellation concentration than Resort Hotels
- OTA-driven bookings contribute significantly to cancellation volume
- Revenue exposure is concentrated in a small number of booking patterns
"""
)

st.markdown("### 📌 Business Objective")

st.write(
    """
This analysis identifies booking behavior patterns that lead to cancellations
and provides actionable recommendations to reduce revenue loss and improve occupancy planning.
"""
)

st.markdown("---")

# ----------------------------
# KPI DISPLAY
# ----------------------------
col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Bookings", kpis["total_bookings"])
col2.metric("Cancelled Bookings", kpis["cancelled"])
col3.metric("Cancellation Rate (%)", f"{kpis['cancellation_rate']:.2f}")
col4.metric("Avg ADR", f"{kpis['avg_adr']:.2f}")

st.markdown("---")

# st.markdown("## 📊 Understanding the Problem")
section_title("Understanding the Problem")

st.markdown("### 1. Where are cancellations happening?")

col1, col2 = st.columns(2)

with col1:
    fig1 = plot_cancellation_by_hotel(filtered_df)
    st.plotly_chart(fig1, use_container_width=True)
    # st.info(insight_hotel(filtered_df))
    st.info(hotel_insight(filtered_df))

with col2:
    fig2 = plot_monthly_cancellation(filtered_df)
    st.plotly_chart(fig2, use_container_width=True)
    st.info(insight_month(filtered_df))

st.markdown("### 2. Who is cancelling?")

fig3 = plot_market_segment(filtered_df)
st.plotly_chart(fig3, use_container_width=True)
st.info(insight_market(filtered_df))

st.info(segment_insight(filtered_df))

st.markdown("---")

# st.markdown("## 🧠 Why Do Cancellations Happen? (Root Cause Analysis)")
section_title("Why Do Cancellations Happen?")

col1, col2 = st.columns(2)

with col1:
    fig1 = plot_lead_time(filtered_df)
    st.plotly_chart(fig1, use_container_width=True)
    # st.info(insight_lead_time(filtered_df))
    st.info(lead_time_insight(filtered_df))

with col2:
    fig2 = plot_deposit_type(filtered_df)
    st.plotly_chart(fig2, use_container_width=True)
    # st.info(insight_deposit(filtered_df))
    st.info(deposit_insight(filtered_df))

col3, col4 = st.columns(2)

with col3:
    fig3 = plot_customer_type(filtered_df)
    st.plotly_chart(fig3, use_container_width=True)
    st.info(insight_customer(filtered_df))

with col4:
    fig4 = plot_previous_cancellations(filtered_df)
    st.plotly_chart(fig4, use_container_width=True)
    st.info(insight_previous(filtered_df))

st.markdown("---")

# st.markdown("## 💰 Business Impact (Revenue Perspective)")
section_title("Business Impact")

col1, col2 = st.columns(2)

with col1:
    fig1 = plot_adr_by_cancellation(filtered_df)
    st.plotly_chart(fig1, use_container_width=True)
    st.info(
        "Canceled bookings show different ADR behavior, "
        "indicating that pricing and cancellation are linked in booking decisions."
    )

with col2:
    fig2 = plot_revenue_risk_by_hotel(filtered_df)
    st.plotly_chart(fig2, use_container_width=True)

    st.info(revenue_insight(filtered_df))
    # st.info(
    #     "City Hotels carry a larger share of potential revenue exposure "
    #     "due to higher cancellation volume."
    # )

st.markdown("### 🔥 Cancellation Risk Heatmap")

fig3 = plot_segment_heatmap(filtered_df)
st.plotly_chart(fig3, use_container_width=True)

st.info(
    "Certain combinations of hotel type and market segment "
    "show significantly higher cancellation risk, indicating targeted intervention opportunities."
)

st.markdown("---")

# st.markdown("## 🧾 Executive Summary & Recommendations")
section_title("Executive Summary & Recommendations")

st.markdown("### 🎯 High-Risk Booking Profile")

persona = high_risk_persona(filtered_df)

for p in persona:
    st.write("•", p)

st.markdown("---")

st.markdown("### 💡 Business Recommendations")

recommendations = generate_recommendations(filtered_df)

for r in recommendations:
    st.success(r)

st.markdown("---")

# st.markdown("## 🏁 Final Conclusion")
section_title("Final Conclusion")

st.info(
    "This analysis shows that hotel booking cancellations are driven by a combination of "
    "lead time, deposit type, and customer segmentation. "
    "By targeting high-risk booking patterns with policy adjustments and customer engagement strategies, "
    "the hotel can significantly reduce cancellation rates and improve revenue predictability."
)

from utils.risk_score import calculate_risk_score

st.markdown("---")
st.header("🎯 Booking Risk Score")

lead = st.slider(
    "Lead Time (Days)",
    0,
    700,
    90
)

deposit = st.selectbox(
    "Deposit Type",
    filtered_df["deposit_type"].unique()
)

previous = st.slider(
    "Previous Cancellations",
    0,
    20,
    0
)

repeat = st.selectbox(
    "Repeated Guest",
    [0,1],
    format_func=lambda x:"Yes" if x==1 else "No"
)

requests = st.slider(
    "Special Requests",
    0,
    5,
    1
)

score = calculate_risk_score(
    lead,
    deposit,
    previous,
    repeat,
    requests
)

st.metric(
    "Booking Risk Score",
    f"{score}/100"
)

if score < 30:
    st.success("🟢 Low Cancellation Risk")

elif score < 60:
    st.warning("🟡 Medium Cancellation Risk")

else:
    st.error("🔴 High Cancellation Risk")

from utils.pdf_report import Report

def create_pdf(kpis):

    pdf = Report()

    pdf.add_page()

    pdf.chapter("Executive Summary")

    pdf.body(
        f"""
Total Bookings : {kpis['total_bookings']}

Cancelled Bookings : {kpis['cancelled']}

Cancellation Rate : {kpis['cancellation_rate']:.2f}%

Average ADR : {kpis['avg_adr']:.2f}

Potential Revenue Associated with Canceled Bookings : {kpis['revenue_loss']:.2f}
"""
    )

    pdf.chapter("Business Conclusion")

    pdf.body(
"""
The analysis identified that longer lead times,
absence of deposits,
and specific market segments
are associated with higher cancellation rates.

Recommended Actions

-> Improve deposit policies

-> Encourage loyalty

-> Send reminder emails

-> Focus retention on high-risk bookings
"""
    )

    pdf.output("Hotel_Report.pdf")

import os

if st.button("📄 Generate Executive Report"):

    create_pdf(kpis)

    with open("Hotel_Report.pdf","rb") as file:

        st.download_button(
            "Download Report",
            file,
            file_name="StayWise_Report.pdf"
        )

# Placeholder for next stages
# st.info("Stage 1 complete: Foundation setup ready. Next we will add storytelling visuals.")