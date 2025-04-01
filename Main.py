import streamlit as st

st.set_page_config(page_title="Market Insights Dashboard", layout="wide")
st.markdown(
    """
    <style>
        [data-testid="stAppViewContainer"] {
            background-color: lightblue;  /* light blue */
        }

        /* Title styling */
        .title {
            color: #4a90e2;
            text-align: center;
            font-size: 36px;
            font-weight: bold;
        }

        /* Upload section */
        .upload-box {
            background-color: #ffffff;
            padding: 15px;
            border-radius: 10px;
            box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
        }

        /* Data Preview Box */
        .data-preview {
            border: 2px solid #4a90e2;
            border-radius: 10px;
            padding: 10px;
            background-color: #ffffff;
        }

        /* Processing message */
        .processing {
            font-size: 16px;
            font-weight: bold;
            color: #ff9800;
            text-align: center;
        }

        /* Response Box */
        .response-box {
            border-radius: 10px;
            background-color: #eef7ff;
            padding: 15px;
        }

        /* Styled Button */
        .stButton>button {
            background-color: #4CAF50 !important;
            color: white !important;
            font-size: 16px;
            border-radius: 10px;
            padding: 10px 20px;
        }
    </style>
    """,
    unsafe_allow_html=True
)


st.title("🏪 Market Insights - Home Page")
st.write("Welcome to the retail analytics dashboard!")

st.sidebar.success("Select a page from the sidebar to navigate.")
