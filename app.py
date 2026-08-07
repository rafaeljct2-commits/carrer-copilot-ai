import streamlit as st
from utilitarios.pdf_reader import extract_text

st.set_page_config(
    page_title="Career Copilot AI",
    page_icon="🚀"
)

st.title("🚀 Career Copilot AI")

uploaded_file = st.file_uploader(
    "Upload Resume PDF",
    type=["pdf"]
)

if uploaded_file:

    text = extract_text(uploaded_file)

    st.success("Resume uploaded successfully!")

    st.subheader("Resume Content")

    st.text_area(
        "Extracted Text",
        text,
        height=300
    )
