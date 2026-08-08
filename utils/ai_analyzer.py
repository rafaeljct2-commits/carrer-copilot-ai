import os
from openai import OpenAI

def analyze_resume(text):

    try:
        client = OpenAI(
            api_key=os.getenv("OPENAI_API_KEY")
        )

        prompt = f"""
        Analyze the following resume.

        Return:

        1. Professional summary
        2. Strengths
        3. Missing skills
        4. Career recommendations

        Resume:

        {text}
        """

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"Error: {str(e)}"
