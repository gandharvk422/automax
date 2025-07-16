# utils/email.py

import resend
import os

resend.api_key = os.getenv("RESEND_API_KEY")

def send_resend_email(to_email, subject, html_content):
    return resend.Emails.send({
        "from": os.getenv("FROM_EMAIL"),
        "to": to_email,
        "subject": subject,
        "html": html_content
    })