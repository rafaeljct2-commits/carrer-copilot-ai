from langdetect import detect

def detect_language(text):
    try:
        language = detect(text)

        languages = {
            "pt": "Portuguese",
            "en": "English",
            "es": "Spanish",
            "fr": "French",
            "de": "German",
            "it": "Italian"
        }

        return languages.get(language, language)

    except:
        return "Unknown"
