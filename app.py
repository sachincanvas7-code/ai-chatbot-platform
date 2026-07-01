"""
RoastMyPM — Step 3: memory (chat UI + conversation history).

What changed from Step 2:
- Text area + button replaced with a proper chat interface
- Conversation history stored in st.session_state.messages
- Full history sent to backend on every message (that's how memory works)
"""

import streamlit as st
from backend import get_response

st.set_page_config(page_title="RoastMyPM", page_icon="🔥")

st.title("🔥 RoastMyPM")
st.caption("The brutally honest résumé coach for product managers")

# Initialize conversation history on first load
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display the full conversation so far
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Chat input box (appears at the bottom)
user_input = st.chat_input("Paste a résumé bullet or ask a follow-up...")

if user_input:
    # 1. Add user message to history and show it
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)

    # 2. Send full history to backend, get roast
    with st.chat_message("assistant"):
        with st.spinner("Roasting..."):
            reply = get_response(st.session_state.messages)
        st.write(reply)

    # 3. Add assistant reply to history
    st.session_state.messages.append({"role": "assistant", "content": reply})
