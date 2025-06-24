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

# App title and styling
st.markdown(
    """
    <style>
    .main-container {
        background: linear-gradient(to bottom right, #f2f8ff, #e6ecf9);
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0px 4px 12px rgba(0,0,0,0.1);
    }
    .title {
        font-size: 36px;
        font-weight: 700;
        color: #2c3e50;
        text-align: center;
    }
    .subtitle {
        text-align: center;
        color: #7f8c8d;
        margin-top: -10px;
    }
    .result {
        background-color: #ffffff;
        border-left: 6px solid #3498db;
        padding: 20px;
        margin-top: 20px;
        border-radius: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

with st.container():
    st.markdown("<div class='main-container'>", unsafe_allow_html=True)
    st.markdown("<div class='title'>🎯 AI Virtual Career Counsellor</div>", unsafe_allow_html=True)
    st.markdown("<div class='subtitle'>Get personalized career recommendations based on your interests.</div>", unsafe_allow_html=True)

    name = st.text_input("👤 Enter your name:", placeholder="e.g. Soham")
    interest_input = st.text_input("💡 What are your interests?", placeholder="e.g. coding, biology, finance")

    if st.button("🔍 Get Career Recommendations"):
        if not name or not interest_input:
            st.warning("Please enter both name and interests to get recommendations.")
        else:
            # Preprocess
            user_keywords = [word.strip().lower() for word in word_tokenize(interest_input)]

            best_match = None
            highest_match_count = 0

            for index, row in df.iterrows():
                row_keywords = [kw.strip().lower() for kw in row['Interest'].split(",")]
                match_count = len(set(user_keywords) & set(row_keywords))
                if match_count > highest_match_count:
                    highest_match_count = match_count
                    best_match = row

            if best_match is not None:
                st.markdown(f"""
                <div class="result">
                <h4>👋 Hi {name}, based on your interests, here’s what we suggest:</h4>
                <b>🎓 Recommended Careers:</b> {best_match['Recommended_Careers']}<br>
                <b>📘 Description:</b> {best_match['Description']}
                </div>
                """, unsafe_allow_html=True)
            else:
                st.error("Sorry, we couldn't find a matching career. Please try different interests.")
    st.markdown("</div>", unsafe_allow_html=True)
