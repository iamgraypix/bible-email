import requests
import os


def get_reflection(verse_text, verse_reference):
    response = requests.post(
        "https://api.groq.com/openai/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {os.environ.get('GROQ_API_KEY')}",
            "Content-Type": "application/json"
        },
        json={
            "model": "llama-3.3-70b-versatile",
            "messages": [
                {
                    "role": "user",
                    "content": f"Given this Bible verse: '{verse_text}' - {verse_reference}. Write a short 3 sentence devotional reflection. Explain what it means and one practical way to apply it in daily life. Keep it warm, encouraging and simple."
                }
            ]
        }
    )
    response.raise_for_status()
    data = response.json()
    return data["choices"][0]["message"]["content"]
