def detect_language(text):

    text = text.lower()

    english_words = [
        "experience",
        "education",
        "skills",
        "english",
        "work",
        "manager",
        "project",
        "professional"
    ]

    score = 0

    for word in english_words:
        if word in text:
            score += 1

    if score >= 2:
        return "English"

    return "Português"
