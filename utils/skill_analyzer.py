def analyze_skills(text):

    text = text.lower()

    skills_database = {
        "English": [
            "english",
            "ingles",
            "inglês"
        ],

        "Administration": [
            "administration",
            "administração",
            "administracao"
        ],

        "Logistics": [
            "logistics",
            "logistic",
            "logística",
            "logistica"
        ],

        "Microsoft Office": [
            "microsoft office",
            "office",
            "word",
            "excel",
            "powerpoint",
            "pacote office"
        ],

        "Digital Marketing": [
            "digital marketing",
            "marketing digital"
        ],

        "Artificial Intelligence": [
            "artificial intelligence",
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
        ],

        "Data Analysis": [
            "data analysis",
            "data analyst",
            "analytics"
        ]
    }

    found_skills = []

    for skill, keywords in skills_database.items():
        for keyword in keywords:
            if keyword in text:
                found_skills.append(skill)
                break

    return found_skills
