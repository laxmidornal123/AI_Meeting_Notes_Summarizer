import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")


def summarize_text(text):

    if len(text.strip()) < 50:
        return text

    prompt = f"""
You are an AI Meeting Assistant.

Summarize the following meeting transcript.

Provide:
1. Summary
2. Key Points
3. Action Items

Transcript:
{text}
"""

    response = model.generate_content(prompt)

    return response.text