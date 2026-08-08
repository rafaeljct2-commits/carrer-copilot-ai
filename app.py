import streamlit as st

from utils.pdf_reader import extract_text
from utils.skill_analyzer import analyze_skills
from utils.language_detector import detect_language

st.set_page_config(page_title="Career Copilot AI")

st.title("Career Copilot AI")

uploaded_file = st.file_uploader(
    "Upload your resume (PDF)",
    type=["pdf"]
)

if uploaded_file:

    text = extract_text(uploaded_file)

    language = detect_language(text)

    st.subheader("Detected Language")
    st.success(language)

    st.subheader("Extracted Resume Text")
    st.write(text)

    skills = analyze_skills(text)

    st.subheader("Skills Identified")

    if skills:
        for skill in skills:
            st.success(skill)
    else:
        st.warning("No skills found.")

    st.subheader("Recommendations")

    recommendations = []

    if "Python" not in skills:
        recommendations.append("Learn Python")

    if "SQL" not in skills:
        recommendations.append("Learn SQL")

    if "Power BI" not in skills:
        recommendations.append("Learn Power BI")

    if "English" not in skills:
        recommendations.append("Improve English")

    for recommendation in recommendations:
        st.info(recommendation)

  
