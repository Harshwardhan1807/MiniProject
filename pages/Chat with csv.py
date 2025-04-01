import langchain.llms
import streamlit as st
from langchain_groq import ChatGroq
import pandas as pd
import os
from dotenv import load_dotenv
from langchain_experimental.agents import create_pandas_dataframe_agent
from langchain.agents import AgentType
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
os.environ["GROQ_API_KEY"] = ""

llm = ChatGroq(temperature=0.2,groq_api_key=api_key,model_name="llama3-70b-8192")

custom_prompt = """
You are an AI assistant analyzing customers' data. Answer questions with accurate insights. 
Avoid answering unrelated questions or making up answers. If you are not able to find just say so and dont make up answer.
Don't repeat the information that you have already given in the output. Don't summarize the information in output keep it as it is.
Don't think repeatedly, if you are unable to find correct ans just stop.If the user asks for a detailed report give ** atleast 10 to 15 sentences **.
Never give only numerical data in analysis consider other categorical columns as well. Give your final thought as the final ans dont summarize it.

Output:
{A detailed report}
"""



st.set_page_config(page_title="Analysis Agent", page_icon="📊", layout="wide")
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
# Title and description
st.title("📊 Analysis Agent")
st.markdown(
    "Upload a CSV file and ask questions about your data. "
    "Our AI-powered agent will analyze and provide insights! 🚀"
)

# File uploader
uploaded_file = st.file_uploader("📂 Upload a CSV file", type=["csv"])

# If a file is uploaded
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    # Display file details
    st.success("✅ File uploaded successfully!")
    st.subheader("🔍 Data Preview")
    st.dataframe(df.head())  # Better UI with st.dataframe()

    # Create the AI agent
    agent = create_pandas_dataframe_agent(
        llm, df, verbose=True, 
        agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        handle_parsing_errors=True,
        allow_dangerous_code=True
    )

    # Input field for user query
    st.subheader("💡 Ask a question about your data")
    query = st.text_input("🔎 Enter your question below:", key="query")

    # Button to get an answer
    if st.button("💬 Get Answer", key="button"):
        if query:
            message = st.empty()
            message.info("⌛ Processing your request...")

            response = agent.run(custom_prompt + query)

            message.empty()  # Remove processing message
            st.subheader("📌 Response")
            st.text_area("📝 AI's Answer", value=response, height=300, disabled=True)



