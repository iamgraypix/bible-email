def generateSubject():
    return "📖 Your Morning Bible Verse"


def generateBody(verse_text, verse_reference, reflection):
    body = f"""
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body style="margin:0; padding:0; background-color:#f4f0eb; font-family: Georgia, serif;">
    <div style="max-width:600px; width:100%; margin:0 auto;">

        <!-- Header -->
        <div style="background: linear-gradient(135deg, #1a1a2e, #16213e); padding:40px 20px; text-align:center;">
            <p style="color:#c9a84c; font-size:12px; letter-spacing:4px; margin:0 0 10px 0;">DAILY SCRIPTURE</p>
            <h1 style="color:#ffffff; font-size:22px; margin:0;">Good Morning 🌅</h1>
        </div>

        <!-- Verse Card -->
        <div style="background:#fdf8f0; border-left: 5px solid #c9a84c; margin:20px 15px; padding:20px; border-radius:8px;">
            <p style="font-size:18px; color:#2c2c2c; line-height:1.8; margin:0 0 15px 0;">"{verse_text}"</p>
            <p style="font-size:14px; color:#c9a84c; font-weight:bold; margin:0 0 20px 0;">— {verse_reference}</p>
            <hr style="border:none; border-top:1px solid #e8dcc8; margin: 20px 0;">
            <p style="font-size:14px; color:#555; line-height:1.8; margin:0;"><strong>Reflection:</strong> {reflection}</p>
        </div>

        <!-- Footer -->
        <div style="padding:20px 15px 40px; text-align:center;">
            <p style="color:#999; font-size:12px;">Have a blessed and wonderful day 🙏</p>
        </div>

    </div>
</body>
</html>
    """
    return body
