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
st.markdown(
    "<h1 style='color: #05074f;'>Peak Hour Analysis</h1>",
    unsafe_allow_html=True
)
st.markdown(
    """
    <style>
    .stFileUploader > label {
        display: none;
    }
    </style>
    """,
    unsafe_allow_html=True
)
uploaded_file = st.file_uploader("📂 Upload a CSV file", type=["csv"])

if uploaded_file:
    # Read the CSV and parse the 'date' and 'time' columns as strings
    df = pd.read_csv(uploaded_file)
    
    # Ensure 'time' is a string and extract hour from 'time' column
    df['hour'] = pd.to_datetime(df['time'], format='%H:%M:%S').dt.hour

    # Count the number of visitors per hour
    hourly_counts = df.groupby('hour').size()

    # Plot the hourly visitor count
    plt.figure(figsize=(10, 5))
    sns.lineplot(x=hourly_counts.index, y=hourly_counts.values, marker='o', color='b')
    plt.xticks(range(9, 21))  # Adjust to show hours from 9 AM to 9 PM
    plt.xlabel("Hour of the Day") 
    plt.ylabel("Number of Visitors")
    plt.title("Customer Footfall by Hour")
    st.pyplot(plt)
    
    df['hour'] = pd.to_datetime(df['time'], format='%H:%M:%S').dt.hour

    # Ensure 'date' is in proper date format
    df['date'] = pd.to_datetime(df['date']).dt.date

    # Filter for hours between 9 AM and 9 PM
    df = df[(df['hour'] >= 9) & (df['hour'] <= 21)]

    # Group by date and hour and count visitors
    hourly_visits = df.groupby(['date', 'hour']).size().unstack(fill_value=0)

    # Plot heatmap
    plt.figure(figsize=(12, 6))
    sns.heatmap(hourly_visits.T, cmap="Blues", annot=True, fmt="d", linewidths=0.5)
    plt.xlabel("Date")
    plt.ylabel("Hour of the Day")
    plt.title("Peak Hour Analysis (9 AM - 9 PM)")
    plt.yticks(rotation=0)
    plt.tight_layout()
    st.pyplot(plt)