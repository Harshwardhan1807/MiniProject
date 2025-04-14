import streamlit as st

st.set_page_config(page_title="Market Insights Dashboard", layout="wide")
st.markdown(
    """
    <style>
        [data-testid="stAppViewContainer"] {
            background-color: lightblue;  
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    "<h1 style='color: #05074f;'>🏪 Market Insights - Home Page</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<h5 style = 'color: #05074f;'>Welcome to Market Insights Dashboard!</h5>",
    unsafe_allow_html=True
)

st.sidebar.success("Select a page from the sidebar to navigate.")
