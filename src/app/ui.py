import streamlit as st

from ..tracker.analyze import analyze_text
from ..tracker.viz import plot_daily_trend

st.set_page_config(page_title="AI Mood Tracker", page_icon="🧠", layout="centered")

st.title("AI Mood Tracker — MVP")
txt = st.text_area("Write your journal entry of the day:", height=150)
if st.button("Analyze"):
    if txt.strip():
        res = analyze_text(txt)
        st.success(f"Sentiment: {res['label']} | score: {res['score']:.2f}")
        p = plot_daily_trend()
        if p:
            st.image(p, caption="Daily trend")
    else:
        st.warning("Text is empty.")
