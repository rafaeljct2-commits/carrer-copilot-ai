import streamlit as st

from utils.pdf_reader import extract_text

st.set_page_config(page_title="Career Copilot AI")

st.title("Career Copilot AI")

uploaded_file = st.file_uploader(
    "Upload your resume (PDF)",
    type=["pdf"]
)

if uploaded_file:
    text = extract_text(uploaded_file)

    st.subheader("Extracted Resume Text")

    st.write(text)
