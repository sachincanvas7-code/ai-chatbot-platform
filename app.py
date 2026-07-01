"""
RoastMyPM — Step 1: the UI (static reply, no LLM yet).

This is the FRONTEND (the "View"). It collects a résumé, hands it to the
backend's get_response(), and shows whatever comes back. Right now the backend
returns a fixed placeholder — proving the wiring works before we add the LLM.
"""

import streamlit as st
from backend import get_response

# Page metadata (browser tab title + icon)
st.set_page_config(page_title="RoastMyPM", page_icon="🔥")

# Header
st.title("🔥 RoastMyPM")
st.caption("The brutally honest résumé coach for product managers")

# 1. A box for the user to paste their résumé (or one bullet)
resume_text = st.text_area(
    "Paste a résumé bullet — or your whole résumé:",
    height=160,
    placeholder="e.g. Managed stakeholders and worked on the product roadmap...",
)

# 2. When they click the button, send the text to the backend and show the reply
if st.button("Roast it 🔥"):
    verdict = get_response(resume_text)
    st.markdown("**The verdict:**")
    st.write(verdict)
