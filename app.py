# app.py

import streamlit as st
import os

os.environ["TRANSFORMERS_NO_TF"] = "1"
from news_checker import analyze_headline

# App title and layout
st.set_page_config(page_title="REAL TIME FAKE NEWS DETECTION", layout="centered")

st.markdown("""
<h1 style='text-align:center; color:#28a745;'>🧠 REAL TIME FAKE NEWS DETECTION</h1>
<p style='text-align:center;'>Detects fake news by comparing meaning — not just keywords.</p>
""", unsafe_allow_html=True)

# Input
user_input = st.text_input("### 📰 Enter a news headline:")

# Centered button
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    analyze_pressed = st.button("🔍 Analyze")

# Results
if analyze_pressed:
    if not user_input.strip():
        st.warning("Enter a valid headline.")
    else:
        result = analyze_headline(user_input)

        icon = "✅" if result["prediction"] == "REAL" else "❌"
        verdict_color = "#D4EDDA" if result["prediction"] == "REAL" else "#F8D7DA"

        st.markdown(f"""
        <div style='background-color:{verdict_color}; padding:10px; border-radius:10px;'>
            <h3 style='color:#000000;'> {icon} Final Verdict: {result['prediction']} </h3>
        </div>
        """, unsafe_allow_html=True)

        st.markdown(f"**🔍 Semantic Similarity Score:** `{result['similarity_score']}`")

        st.markdown("### 📰 Top Matching News Articles:")
        for article in result["matching_articles"]:
            st.markdown(f"**{article['title']}**")
            st.markdown(f"🔗 [Read Full Article]({article['url']})", unsafe_allow_html=True)
