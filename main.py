import streamlit as st
import pandas as pd
import nltk
from nltk.tokenize import word_tokenize
import nltk

nltk.download('punkt')


nltk.download('punkt')

# Load dataset
df = pd.read_csv("interest_recommended_careers_with_descriptions.csv") 

# Page setup
st.set_page_config(page_title="AI Career Counsellor", layout="centered")

# Add gradient background and container styling
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #f5f7fa, #c3cfe2);
        background-attachment: fixed;
        font-family: 'Segoe UI', sans-serif;
    }

    .main-container {
        background-color: rgba(255, 255, 255, 0.85);
        padding: 2rem;
        border-radius: 1rem;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
        max-width: 700px;
        margin: 2rem auto 2.5rem auto;
    }

    .stTextInput > div > div > input {
        color: #333;
        font-weight: 500;
    }

    h1, h2, h3, h4 {
        color: #1c1c1c;
        margin-bottom: 1.5rem;
    }

    .stButton button {
        background-color: #4a90e2;
        color: white;
        font-weight: bold;
        border-radius: 8px;
    }

    .stButton button:hover {
        background-color: #357ABD;
    }
    </style>

    <div class="main-container">
        <h1>🎯 AI Virtual Career Counsellor</h1>
    """,
    unsafe_allow_html=True
)

# Input Form
with st.form("career_form"):
    name = st.text_input("Your Name")
    interest = st.text_input("What's something you enjoy or are interested in? (e.g., coding, design, biology)")
    submitted = st.form_submit_button("Find My Career Path")

if submitted:
    if not interest.strip():
        st.warning("Please enter an interest.")
    else:
        user_keywords = [word.strip().lower() for word in word_tokenize(interest)]

        matched_row = None
        for _, row in df.iterrows():
            row_interest = row['Interest'].strip().lower()
            if any(kw in row_interest for kw in user_keywords):
                matched_row = row
                break

        if matched_row is not None:
            st.success(f"🧠 Based on your interest, here's what we found!")

            st.markdown(f"""
            ### You seem to be interested in: **{matched_row['Interest'].title()}**

            **🔍 Recommended Careers:**
            - {', '.join([career.strip() for career in matched_row['Recommended_Careers'].split(',')])}

            **📘 What it involves:**
            > {matched_row['Description']}
            """)
        else:
            st.error("Sorry! We couldn’t find a perfect match. Try rephrasing your interest or using a simpler keyword.")

# Close the content wrapper div
st.markdown("</div>", unsafe_allow_html=True)
