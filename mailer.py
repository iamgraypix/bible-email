import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email_builder import generateSubject, generateBody


def send_email(verse_text, verse_reference, reflection):
    subject = generateSubject()
    body = generateBody(verse_text, verse_reference, reflection)

    sender = os.environ.get("SENDER_EMAIL")
    receiver = os.environ.get("RECEIVER_EMAIL")
    password = os.environ.get("SENDER_PASSWORD")

    msg = MIMEMultipart()
    msg["From"] = f"God's Word 📖 <{sender}>"
    msg["To"] = receiver
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "html"))

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender, password)
        server.sendmail(sender, receiver, msg.as_string())
        print("Email sent successfully!")
