import streamlit as st
import requests
from config import PAGE_TITLE, PAGE_ICON, CHAT_ENDPOINT

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON, layout="centered")

st.title(f"{PAGE_ICON} {PAGE_TITLE}")

# Initialize chat session history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Sidebar options
with st.sidebar:
    st.header("Settings & Tools")
    if st.button("Clear Conversation", use_container_width=True):
        st.session_state.messages = []
        st.rerun()
    st.markdown("---")
    st.caption("Powered by Google Gemini & FastAPI")

# Display message history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

user_input = st.chat_input("Type your message here...")

if user_input:
    history_to_send = list(st.session_state.messages)

    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    with st.chat_message("user"):
        st.write(user_input)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                response = requests.post(
                    CHAT_ENDPOINT,
                    json={
                        "message": user_input,
                        "history": history_to_send
                    },
                    timeout=60
                )
                
                if response.status_code == 200:
                    data = response.json()
                    if data.get("error"):
                        bot_reply = f"⚠️ API Error: {data['error']}"
                    else:
                        bot_reply = data.get("response", "No response returned.")
                else:
                    bot_reply = f"⚠️ HTTP Error {response.status_code}: Unable to reach backend server."

            except requests.exceptions.RequestException as e:
                bot_reply = f"⚠️ Connection Error: Could not connect to backend at {CHAT_ENDPOINT}. Is the server running?"

            st.write(bot_reply)

    st.session_state.messages.append(
        {"role": "assistant", "content": bot_reply}
    )
