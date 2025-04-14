import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import chardet
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
    "<h1 style='color: #05074f;'>Gender Analysis</h1>",
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
    raw_data = uploaded_file.read()

    # Detect encoding
    result = chardet.detect(raw_data)
    encoding = result['encoding']
    confidence = result['confidence']

    st.write(f"Detected encoding: {encoding} (Confidence: {confidence:.2f})")

    # Go back to the beginning of the file (important!)
    uploaded_file.seek(0)

    # Read using detected encoding
    df = pd.read_csv(uploaded_file, encoding=encoding)

    st.subheader("Gender Distribution")
    gender_counts = df["gender"].value_counts()
    plt.figure(figsize=(3, 3))
    plt.pie(gender_counts, labels=["Male", "Female"], autopct="%1.1f%%", colors=["lightblue", "lightpink"], startangle=90)
    plt.title("Gender Distribution")
    st.pyplot(plt)

    # Countplot to visualize gender distribution across age groups
    age_bins = [0, 18, 35, 50, 100]
    age_labels = ["0-18", "19-35", "36-50", "51+"]

    plt.figure(figsize=(8, 5))
    age_grp = pd.cut(df["age"], bins=age_bins, labels=age_labels, right=False)

    sns.countplot(data=df, x=age_grp, hue="gender", palette=["blue", "pink"])
    plt.xlabel("Age Group")
    plt.ylabel("Count")
    plt.title("Gender Distribution Across Age Groups")
    st.pyplot(plt)
