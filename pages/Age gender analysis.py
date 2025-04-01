import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
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
st.title("🎂 Age & Gender Analysis")

df = pd.read_csv("market_insights_data_variable.csv")


st.subheader("Age Distribution")
plt.figure(figsize=(10, 5))
sns.histplot(df["age"], bins=10, kde=True, color='g')
plt.xlabel("Age")
plt.ylabel("Count")
plt.title("Age Distribution of Customers")
st.pyplot(plt)

st.subheader("Gender Distribution")
gender_counts = df["gender"].value_counts()
plt.figure(figsize=(6, 6))
plt.pie(gender_counts, labels=["Male", "Female"], autopct="%1.1f%%", colors=["blue", "pink"], startangle=90)
plt.title("Gender Distribution")
st.pyplot(plt)
