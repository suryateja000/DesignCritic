import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI

def get_llm(model: str="gemini-2.5-flash", temperature: float=0.3):
    return ChatGoogleGenerativeAI(
        model=model,
        temperature=temperature,
        google_api_key=st.secrets["GOOGLE_API_KEY"],
        max_retries=10,        
    )
