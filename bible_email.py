from dotenv import load_dotenv
from verse import get_bible_verse
from reflection import get_reflection
from mailer import send_email

load_dotenv()

verse_text, verse_reference = get_bible_verse()
reflection = get_reflection(verse_text, verse_reference)
send_email(verse_text, verse_reference, reflection)
