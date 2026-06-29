import streamlit as st

def apply_styles():
    st.markdown("""
    <style>
        .main {
            background-color: #F8FAFC;
        }

        h1, h2, h3 {
            color: #0F172A;
        }

        .metric-card {
            background-color: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0px 2px 10px rgba(0,0,0,0.05);
        }
    </style>
    """, unsafe_allow_html=True)