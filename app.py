import streamlit as st

from utils.pdf_reader import extract_text
from utils.skill_analyzer import analyze_skills

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

    skills = analyze_skills(text)

    st.subheader("Skills Identificadas")

    if skills:
        for skill in skills:
            st.success(skill)
    else:
        st.warning("Nenhuma skill encontrada.")

    st.subheader("Recomendações")

    recommendations = []

    if "python" not in skills:
        recommendations.append("Aprender Python")

    if "sql" not in skills:
        recommendations.append("Aprender SQL")

    if "power bi" not in skills:
        recommendations.append("Aprender Power BI")

    for item in recommendations:
        st.info(item)
