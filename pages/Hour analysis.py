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
st.title("⏳ Peak Hour Analysis")

df = pd.read_csv("market_insights_data_variable.csv", parse_dates=["datetime"])
df["hour"] = df["datetime"].dt.hour

hourly_counts = df.groupby("hour").size()
plt.figure(figsize=(10, 5))
sns.lineplot(x=hourly_counts.index, y=hourly_counts.values, marker='o', color='b')
plt.xticks(range(9, 21))
plt.xlabel("Hour of the Day") 
plt.ylabel("Number of Visitors")
plt.title("Customer Footfall by Hour")
st.pyplot(plt)