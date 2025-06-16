import streamlit as st
from utils.llm import get_response
from utils.prompt import build_prompt

st.set_page_config(page_title="Chatbot", page_icon="🤖")
st.title("🤖 Basic Modular Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Input
if prompt := st.chat_input("Say something..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    full_prompt = build_prompt(prompt)
    response = get_response(full_prompt)

    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.markdown(response)
