# Bible Email

A Python script that automatically sends a daily Bible verse with an AI-generated devotional reflection via email. Runs on a schedule using GitHub Actions.

## How It Works

1. **Fetches a random Bible verse** from [bible-api.com](https://bible-api.com)
2. **Generates a short reflection** using Groq's Llama 3.3 70B model — a warm, 3-sentence devotional with a practical daily application
3. **Sends an HTML email** with the verse and reflection formatted as a styled morning devotional

## Schedule

Emails are sent 6 times a day at Philippine Standard Time (PST):

| UTC | Philippine Time |
|-----|----------------|
| 10:00 PM | 6:00 AM |
| 1:00 AM | 9:00 AM |
| 4:00 AM | 12:00 NN |
| 7:00 AM | 3:00 PM |
| 10:00 AM | 6:00 PM |
| 1:00 PM | 9:00 PM |

## Setup

### Prerequisites

- Python 3.10+
- A Gmail account with an [App Password](https://support.google.com/accounts/answer/185833) enabled
- A [Groq API key](https://console.groq.com)

### Install Dependencies

```bash
pip install requests python-dotenv
```

### Environment Variables

Create a `.env` file (for local runs) or set GitHub Actions secrets:

| Variable | Description |
|----------|-------------|
| `SENDER_EMAIL` | Gmail address to send from |
| `SENDER_PASSWORD` | Gmail App Password |
| `RECEIVER_EMAIL` | Email address to send to |
| `GROQ_API_KEY` | Groq API key for AI reflection |

### Run Locally

```bash
python bible_email.py
```

## GitHub Actions

The workflow at `.github/workflows/send_verse.yml` handles automated scheduling. Add the environment variables as repository secrets under **Settings > Secrets and variables > Actions**.

You can also trigger it manually via **Actions > Daily Bible Verse > Run workflow**.

## Project Structure

```
bible_email.py     # Entry point
verse.py           # Fetches random Bible verse from bible-api.com
reflection.py      # Generates devotional reflection via Groq API
email_builder.py   # Builds HTML email subject and body
mailer.py          # Sends email via Gmail SMTP
```
