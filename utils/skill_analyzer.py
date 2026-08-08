def analyze_skills(text):

    text = text.lower()

    skills_database = {
        "Inglês": [
            "inglês",
            "ingles",
            "english"
        ],

        "Administração": [
            "administração",
            "administracao"
        ],

        "Logística": [
            "logístico",
            "logistica",
            "logística"
        ],

        "Pacote Office": [
            "pacote office",
            "microsoft office",
            "office"
        ],

        "Marketing Digital": [
            "marketing digital"
        ],

        "Inteligência Artificial": [
            "inteligência artificial",
            "inteligencia artificial",
            "ai"
        ],

        "Python": [
            "python"
        ],

        "SQL": [
            "sql"
        ],

        "Power BI": [
            "power bi"
        ]
    }

    found_skills = []

    for skill, keywords in skills_database.items():
        for keyword in keywords:
            if keyword in text:
                found_skills.append(skill)
                break

    return found_skills
  
