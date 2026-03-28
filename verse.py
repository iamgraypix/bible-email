import requests


def get_bible_verse():
    response = requests.get("https://bible-api.com/?random=verse")
    response.raise_for_status()
    data = response.json()
    verse_text = data["text"].strip()
    verse_reference = data["reference"]
    return verse_text, verse_reference
