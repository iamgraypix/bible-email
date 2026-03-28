import os
import requests
from email_builder import generateSubject, generateBody


def send_email(verse_text, verse_reference, reflection):
    subject = generateSubject()
    body = generateBody(verse_text, verse_reference, reflection)

    sender = "God <onboarding@resend.dev>"
    receiver = os.environ.get("RECEIVER_EMAIL").split(",")
    resend_api_key = os.environ.get("RESEND_API_KEY")

    response = requests.post(
        "https://api.resend.com/emails",
        headers={
            "Authorization": f"Bearer {resend_api_key}",
            "Content-Type": "application/json"
        },
        json={
            "from": sender,
            "to": receiver,
            "subject": subject,
            "html": body
        }
    )

    if response.status_code == 200:
        print("Email sent successfully!")
    else:
        print(f"Failed to send email: {response.json()}")


