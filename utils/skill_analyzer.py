def analyze_skills(text):
    skills_database = [
        "python",
        "excel",
        "power bi",
        "sql",
        "ingles",
        "english",
        "marketing digital",
        "logistica",
        "gestao",
        "pacote office",
        "powerpoint",
        "word",
        "ai",
        "inteligencia artificial",
        "machine learning"
    ]

    found_skills = []

    text_lower = text.lower()

    for skill in skills_database:
        if skill in text_lower:
            found_skills.append(skill)

    return found_skills
