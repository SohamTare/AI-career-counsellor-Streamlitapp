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
    <div style='
        background-color: white;
        padding: 2rem 1.5rem;
        border-radius: 20px;
        box-shadow: 0 5px 15px rgba(0,0,0,0.05);
        text-align: center;
        margin-bottom: 30px;
    '>
        <h1 style='font-size: 2.8rem; color: #1e1e2f; font-weight: 800;'>🎯 AI Virtual Career Counsellor</h1>
        <p style='font-size: 1.1rem; color: #5c5f70;'>Get personalized career recommendations based on your interests.</p>
    </div>
""", unsafe_allow_html=True)

# Input form
name = st.text_input("👤 Enter Your Name:")
interest = st.text_input("🧠 What are your interests? (e.g. coding, writing, biology)")

if st.button("🔍 Get Career Recommendations"):
    if interest.strip() != "":
        # Scroll effect with anchor
        st.markdown("<div id='result'></div>", unsafe_allow_html=True)

        # Process
        interest = interest.lower().strip()
        user_keywords = [word.strip().lower() for word in word_tokenize(interest)]

        best_match = None
        highest_match_count = 0
        for index, row in df.iterrows():
            row_keywords = [kw.strip().lower() for kw in row['keywords'].split(",")]
            match_count = len(set(user_keywords) & set(row_keywords))
            if match_count > highest_match_count:
                highest_match_count = match_count
                best_match = row

        if best_match is not None:
            st.markdown("""
                <div style='
                    background-color: #f9fafe;
                    padding: 1.5rem;
                    border-radius: 15px;
                    margin-top: 2rem;
                    box-shadow: 0 5px 10px rgba(0, 0, 0, 0.03);
                '>
                    <h3 style='color: #2b2d42;'>You seem to be interested in: <span style="color:#1985a1;">{}</span></h3>
                    <hr style='margin: 10px 0;' />
                    <p><strong>💼 Recommended Careers:</strong> {}</p>
                    <p><strong>📝 About this Career:</strong> {}</p>
                </div>
            """.format(interest, best_match['Recommended_Careers'], best_match['Description']), unsafe_allow_html=True)
        else:
            st.error("Sorry! We couldn't find a matching career path.")
