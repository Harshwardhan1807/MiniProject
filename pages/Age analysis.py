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
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    "<h1 style='color: #05074f;'>Age Analysis</h1>",
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
    file_name = uploaded_file.name.lower()
    if file_name.endswith('.csv'):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

    st.subheader("Age Distribution")
    plt.figure(figsize=(10, 5))
    sns.histplot(df["age"], bins=10, color='g')
    plt.xlabel("Age")
    plt.ylabel("Count")
    plt.title("Age Distribution of Customers")
    st.pyplot(plt)

    age_bins = [0, 18, 35, 50, 100]
    age_labels = ["0-18", "19-35", "36-50", "51+"]
    age_group = pd.cut(df["age"], bins=age_bins, labels=age_labels, right=False)
    age_distribution = age_group.value_counts().sort_index()
    plt.figure(figsize=(8, 5))
    age_distribution.plot(kind="bar", color="skyblue")
    plt.xlabel("Age Group")
    plt.ylabel("Count")
    plt.title("Age Distribution of Customers")
    plt.xticks(rotation=0)
    st.pyplot(plt) 