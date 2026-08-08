def analyze_skills(text):

    text = text.lower()

    skills_database = {
        "English": [
            "english",
            "ingles",
            "inglês",
            "anglais",
            "englisch"
        ],

        "Python": [
            "python"
        ],

        "SQL": [
            "sql"
        ],

        "Power BI": [
            "power bi"
        ],

        "Logistics": [
            "logistics",
            "logistica",
            "logística",
            "logistique",
            "logistik"
        ],

        "Administration": [
            "administration",
            "administração",
            "administracao",
            "verwaltung",
            "administración"
        ],

        "Artificial Intelligence": [
            "artificial intelligence",
            "inteligência artificial",
            "inteligencia artificial",
            "intelligence artificielle",
            "kunstliche intelligenz",
            "ai"
        ]
    }

    found_skills = []

    for skill, keywords in skills_database.items():
        for keyword in keywords:
            if keyword in text:
                found_skills.append(skill)
                break

    return found_skills
