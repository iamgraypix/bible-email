import smtplib
import requests
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Your email settings
SENDER_EMAIL = "charlesartillero@gmail.com"
SENDER_PASSWORD = "ukhtdogiaglmnzec"
RECEIVER_EMAIL = "charlesartillero@gmail.com"

def get_bible_verse():
    response = requests.get("https://bible-api.com/?random=verse")
    data = response.json()
    verse_text = data["text"].strip()
    verse_reference = data["reference"]
    return verse_text, verse_reference

def generateSubject():
    subject = "📖 Your Morning Bible Verse"
    return subject

def generateBody():
    body = f"""
<html>
    <body style="margin:0; padding:0; background-color:#f4f0eb; font-family: Georgia, serif;">
        <div style="max-width:600px; margin:40px auto; background:#fff; border-radius:16px; overflow:hidden; box-shadow: 0 4px 20px rgba(0,0,0,0.1);">
            
            <!-- Header -->
            <div style="background: linear-gradient(135deg, #1a1a2e, #16213e); padding:40px 30px; text-align:center;">
                <p style="color:#c9a84c; font-size:13px; letter-spacing:4px; margin:0 0 10px 0;">DAILY SCRIPTURE</p>
                <h1 style="color:#ffffff; font-size:26px; margin:0;">Good Morning 🌅</h1>
            </div>

            <!-- Verse Card -->
            <div style="background:#fdf8f0; border-left: 5px solid #c9a84c; margin:40px 30px; padding:30px; border-radius:8px;">
                <p style="font-size:20px; color:#2c2c2c; line-height:1.8; margin:0 0 20px 0;">"{verse_text}"</p>
                <p style="font-size:15px; color:#c9a84c; font-weight:bold; margin:0;">— {verse_reference}</p>
            </div>

            <!-- Footer -->
            <div style="padding:20px 30px 40px; text-align:center;">
                <p style="color:#999; font-size:13px;">Have a blessed and wonderful day 🙏</p>
            </div>

        </div>
    </body>
    </html>
    """
    return body

def send_email(verse_text, verse_reference):
    subject = generateSubject()
    body = generateBody()

    msg = MIMEMultipart()
    msg["From"] = "God's Word 📖" + SENDER_EMAIL
    msg["To"] = RECEIVER_EMAIL
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "html"))

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, msg.as_string())
        print("Email sent successfully!")

verse_text, verse_reference = get_bible_verse()
send_email(verse_text, verse_reference)