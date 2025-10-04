import streamlit as st
import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load API key
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Use Gemini model
model = genai.GenerativeModel("models/gemini-2.5-flash")

# Streamlit UI
st.title("🤖 Gemini General Q&A Bot")
st.write("Ask any question and get answers using Gemini 2.5 Flash model.")

question = st.text_input("Your Question:")

if st.button("Ask") and question:
    try:
        response = model.generate_content(question)
        st.write("**Answer:**", response.text)
    except Exception as e:
        st.error(f"Error: {e}")
