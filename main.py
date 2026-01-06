
---

# ✅ 2️⃣ `main.py` (CLEAN & PROFESSIONAL)

This version **supports BOTH OpenAI & Ollama** in one file.

```python
import os
import streamlit as st
from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Load environment variables
load_dotenv()

# LangSmith Tracking
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = "Q&A Chatbot (OpenAI & Ollama)"

# Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Answer clearly and concisely."),
        ("user", "Question: {question}")
    ]
)

def generate_openai_response(question, model, temperature, max_tokens, api_key):
    llm = ChatOpenAI(
        model=model,
        temperature=temperature,
        max_tokens=max_tokens,
        openai_api_key=api_key
    )
    chain = prompt | llm | StrOutputParser()
    return chain.invoke({"question": question})

def generate_ollama_response(question, model, temperature):
    llm = Ollama(model=model, temperature=temperature)
    chain = prompt | llm | StrOutputParser()
    return chain.invoke({"question": question})

# ------------------ Streamlit UI ------------------

st.title("🧠 Enhanced Q&A Chatbot")

st.sidebar.title("⚙️ Settings")

mode = st.sidebar.selectbox("Select Mode", ["OpenAI (Cloud)", "Ollama (Local)"])

temperature = st.sidebar.slider("Temperature", 0.0, 1.0, 0.7)
max_tokens = st.sidebar.slider("Max Tokens", 50, 300, 150)

if mode == "OpenAI (Cloud)":
    api_key = st.sidebar.text_input("OpenAI API Key", type="password")
    model = st.sidebar.selectbox("Model", ["gpt-4o", "gpt-4o-mini"])
else:
    model = st.sidebar.selectbox("Local Model", ["mistral"])

st.write("### Ask your question:")
user_input = st.text_input("You:")

if user_input:
    try:
        if mode == "OpenAI (Cloud)":
            response = generate_openai_response(
                user_input, model, temperature, max_tokens, api_key
            )
        else:
            response = generate_ollama_response(
                user_input, model, temperature
            )

        st.success(response)

    except Exception as e:
        st.error(str(e))
else:
    st.info("Please enter a question.")
