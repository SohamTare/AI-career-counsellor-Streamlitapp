import streamlit as st
import pandas as pd
import nltk
from nltk.tokenize import word_tokenize
import nltk
nltk.download("punkt")
nltk.download("punkt_tab")  # Safe to include even if not used
nltk.download("averaged_perceptron_tagger")  # Often helpful

# Load dataset
df = pd.read_csv("interest_recommended_careers_with_descriptions.csv") 

# Page setup
st.set_page_config(page_title="AI Career Counsellor", layout="centered")

st.markdown("""
    <style>
    body {
        background: linear-gradient(120deg, #fdfbfb 0%, #ebedee 100%);
        font-family: 'Segoe UI', sans-serif;
    }
    .main-container {
        background-color: #ffffffdd;
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        margin-top: 30px;
    }
    .headline {
        font-size: 2.5rem;
        font-weight: 700;
        text-align: center;
        margin-bottom: 10px;
        color: #2E3A59;
    }
    .subtext {
        font-size: 1rem;
        text-align: center;
        margin-bottom: 30px;
        color: #6c757d;
    }
    .stButton > button {
        background-color: #2E3A59;
        color: white;
        padding: 10px 20px;
        border-radius: 8px;
        font-size: 1rem;
    }
    </style>
""", unsafe_allow_html=True)

# UI Components
st.markdown("<div class='main-container'>", unsafe_allow_html=True)
st.markdown("<div class='headline'>🎯 AI Virtual Career Counsellor</div>", unsafe_allow_html=True)
st.markdown("<div class='subtext'>Get personalized career recommendations based on your interests.</div>", unsafe_allow_html=True)

name = st.text_input("👤 Enter Your Name:")
interest = st.text_input("🧠 What are your interests? (e.g. coding, writing, biology)")

if st.button("🔍 Get Career Recommendations"):
    if name and interest:
        user_keywords = [word.strip().lower() for word in word_tokenize(interest)]

        matched_rows = []
        for _, row in df.iterrows():
            row_keywords = [kw.strip().lower() for kw in row['keywords'].split(",")]
            if any(keyword in row_keywords for keyword in user_keywords):
                matched_rows.append(row)

        if matched_rows:
            st.success(f"Here are some careers for {name.title()} based on your interests:")
            for career in matched_rows:
                st.markdown(f"""
                <div style="background-color:#f9f9f9;padding:15px;border-radius:10px;margin:10px 0;">
                <strong>{career['Recommended_Careers']}</strong><br>
                <small>{career['Description']}</small>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.warning("Sorry! We couldn't find a match. Try different keywords.")
    else:
        st.warning("Please fill in both your name and interests.")
st.markdown("</div>", unsafe_allow_html=True) 
