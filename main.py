import streamlit as st
import pandas as pd

# Load the data
@st.cache_data
def load_data():
    df = pd.read_csv("interest_recommended_careers_with_descriptions.csv")
    df.columns = df.columns.str.strip()  # Clean column names
    return df

df = load_data()

# ---------- Styling -----------
st.markdown("""
    <style>
        body {
            background: linear-gradient(to bottom right, #f7f8fc, #dbefff);
        }
        .title-box {
            background-color: #ffffffcc;
            padding: 30px;
            border-radius: 12px;
            text-align: center;
            box-shadow: 0px 4px 20px rgba(0, 0, 0, 0.1);
            margin-bottom: 30px;
        }
        .result-box {
            background-color: #ffffffcc;
            padding: 20px;
            border-left: 6px solid #1f77b4;
            border-radius: 10px;
            margin-top: 30px;
            font-size: 16px;
        }
        .stTextInput input {
            font-size: 16px !important;
        }
        .stButton button {
            font-size: 16px !important;
            background-color: #1f77b4;
            color: white;
            border-radius: 8px;
            padding: 8px 16px;
        }
    </style>
""", unsafe_allow_html=True)

# ---------- Header ------------
st.markdown("""
    <div class="title-box">
        <h1>🎯 AI Virtual Career Counsellor</h1>
        <p>Get personalized career recommendations based on your interests.</p>
    </div>
""", unsafe_allow_html=True)

# ---------- User Inputs -------
name = st.text_input("👤 Enter your name:")
interest = st.text_input("🧠 What are your interests?", placeholder="e.g. coding, writing, biology")

if st.button("🔍 Get Career Recommendations"):
    if not name or not interest:
        st.warning("⚠️ Please enter both your name and interests.")
    else:
        # Normalize user input (split by commas, strip and lowercase)
        user_keywords = [kw.strip().lower() for kw in interest.split(",") if kw.strip()]

        matched_rows = []

        for _, row in df.iterrows():
            interest_value = row.get('Interest')
            if pd.isna(interest_value):
                continue

            row_keywords = [kw.strip().lower() for kw in str(interest_value).split(",") if kw.strip()]

            # If any user keyword is in row's interest list
            if any(user_kw in row_keywords for user_kw in user_keywords):
                matched_rows.append(row)

        if matched_rows:
            for match in matched_rows:
                st.markdown(f"""
                    <div class="result-box">
                        <h3>👋 Hi {name.title()}!</h3>
                        <p><strong>🎯 Recommended Careers:</strong> {match['Recommended_Careers']}</p>
                        <p><strong>📄 Description:</strong> {match['Description']}</p>
                    </div>
                """, unsafe_allow_html=True)
        else:
            st.error("❌ No matching careers found. Try using broader or more common interest keywords.")
