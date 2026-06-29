# import streamlit as st

# def apply_ui():
#     st.markdown("""
#     <style>

#     /* Background */
#     .stApp {
#         background-color: #F8FAFC;
#     }

#     /* KPI Cards */
#     div[data-testid="metric-container"] {
#         background-color: white;
#         border-radius: 12px;
#         padding: 16px;
#         box-shadow: 0 2px 10px rgba(0,0,0,0.05);
#     }

#     /* Titles */
#     h1, h2, h3 {
#         color: #0F172A;
#         font-family: 'Segoe UI';
#     }

#     /* Sidebar */
#     section[data-testid="stSidebar"] {
#         background-color: #0F172A;
#     }

#     /* Sidebar text */
#     section[data-testid="stSidebar"] * {
#         color: white;
#     }

#     /* Info boxes */
#     .stAlert {
#         border-radius: 10px;
#     }

#     </style>
#     """, unsafe_allow_html=True)

import streamlit as st

def apply_ui():
    st.markdown("""
    <style>

    /* Global background */
    .stApp {
        background-color: #F8FAFC;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background-color: #0F172A;
    }

    section[data-testid="stSidebar"] * {
        color: white;
    }

    /* Main title styling */
    h1 {
        color: #0F172A;
        font-weight: 700;
    }

    h2 {
        color: #1F2937;
        border-bottom: 2px solid #E5E7EB;
        padding-bottom: 5px;
        margin-top: 25px;
    }

    /* KPI Cards */
    div[data-testid="metric-container"] {
        background-color: white;
        border-radius: 14px;
        padding: 18px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.06);
        border: 1px solid #E5E7EB;
    }

    /* Info boxes */
    div.stAlert {
        border-radius: 12px;
        border-left: 4px solid #2563EB;
    }

    /* Success boxes */
    div.stAlert[data-baseweb="notification"][kind="success"] {
        border-left: 4px solid #10B981;
    }

    /* Warning boxes */
    div.stAlert[data-baseweb="notification"][kind="warning"] {
        border-left: 4px solid #F59E0B;
    }

    /* Error boxes */
    div.stAlert[data-baseweb="notification"][kind="error"] {
        border-left: 4px solid #DC2626;
    }

    </style>
    """, unsafe_allow_html=True)


def section_title(title):
    st.markdown(f"## {title}")
    st.markdown("---")


def spacer(n=1):
    for _ in range(n):
        st.write("")