# main.py
import streamlit as st
from utils.prompt_templates import *
from utils.llm import generate_completion

# Set Streamlit page config FIRST
st.set_page_config(page_title="Performance Evaluation AI Assistant", layout="wide")

# -- API Key Authentication --
if "api_key" not in st.session_state:
    st.session_state.api_key = ""

st.title("🔒 Performance Evaluation Assistant Login")

if not st.session_state.api_key:
    api_key_input = st.text_input("Enter your OpenAI API key:", type="password")
    if st.button("Submit"):
        if api_key_input.startswith("sk-"):
            st.session_state.api_key = api_key_input
        else:
            st.error("Please enter a valid OpenAI API key.")
    st.stop()

# -- App Content After Auth --
st.title("📈 Performance Evaluation Assistant")

section = st.selectbox("Which section do you want help with?", [
    "Goals", "Achievements", "Rating Justification",
    "Job Knowledge", "Service Excellence", "Compliance and Accountability",
    "Communication and Interpersonal Skills", "Efficiency", "Management and Leadership"
])

input_text = st.text_area("Enter your rough notes or bullet points here:")

if section == "Rating Justification":
    rating = st.selectbox("Select your self-rating:", ["Meets Expectations", "Exceeds Expectations", "Needs Improvement"])

if st.button("Generate Polished Text"):
    if not input_text.strip():
        st.warning("Please enter some input text.")
    else:
        if section == "Goals":
            prompt = goal_template.format(input_text=input_text)
        elif section == "Achievements":
            prompt = achievement_template.format(input_text=input_text)
        elif section == "Rating Justification":
            prompt = justification_template.format(rating=rating, input_text=input_text)
        elif section == "Job Knowledge":
            prompt = job_knowledge_template.format(input_text=input_text)
        elif section == "Service Excellence":
            prompt = service_excellence_template.format(input_text=input_text)
        elif section == "Compliance and Accountability":
            prompt = compliance_template.format(input_text=input_text)
        elif section == "Communication and Interpersonal Skills":
            prompt = communication_template.format(input_text=input_text)
        elif section == "Efficiency":
            prompt = efficiency_template.format(input_text=input_text)
        elif section == "Management and Leadership":
            prompt = leadership_template.format(input_text=input_text)

        with st.spinner("Generating..."):
            output = generate_completion(prompt, api_key=st.session_state.api_key)
            st.success("Done!")
            st.text_area("Suggested Text:", value=output, height=200)