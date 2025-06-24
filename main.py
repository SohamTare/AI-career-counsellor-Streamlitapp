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

# Set page config
st.set_page_config(page_title="AI Virtual Career Counsellor", layout="centered")

# Custom background and styling
st.markdown("""
    <style>
    body {
        background: linear-gradient(to bottom, #e0ecf4, #f7f7f7);
    }
    .main-title {
        font-size: 36px;
        font-weight: 700;
        text-align: center;
        padding: 1.5rem;
        border-radius: 10px;
        background-color: #ffffffcc;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        margin-bottom: 30px;
    }
    .input-box {
        background-color: #ffffffdd;
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 20px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown('<div class="main-title">🎯 AI Virtual Career Counsellor</div>', unsafe_allow_html=True)

# Input box
with st.container():
    st.markdown('<div class="input-box">', unsafe_allow_html=True)
    name = st.text_input("Enter your name", placeholder="e.g. Soham")
    interest = st.text_input("What are your interests?", placeholder="e.g. coding, problem solving")
    st.markdown('</div>', unsafe_allow_html=True)

if name and interest:
    st.markdown("---")
    user_keywords = [word.strip().lower() for word in word_tokenize(interest)]

    best_match = None
    highest_match_count = 0

    for _, row in df.iterrows():
        row_keywords = [kw.strip().lower() for kw in row['Interest'].split(",")]
        match_count = len(set(user_keywords) & set(row_keywords))
        if match_count > highest_match_count:
            highest_match_count = match_count
            best_match = row

    if best_match is not None:
        st.markdown(f"## 🚀 Hello {name}, based on your interests:")
        st.markdown(f"### 👨‍💻 Recommended Careers: **{best_match['Recommended_Careers']}**")
        st.markdown(f"#### 📌 Description: {best_match['Description']}")
    else:
        st.warning("Sorry! No matching career found. Try different interests.")
