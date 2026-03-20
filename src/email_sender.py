import os
import json
import smtplib
from email.message import EmailMessage
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def load_config():
    config_path = os.path.join(BASE_DIR, 'config', 'config.json')
    with open(config_path) as f:
        return json.load(f)

def log_status(email, status):
    log_path = os.path.join(BASE_DIR, 'logs', 'email_logs.txt')
    os.makedirs(os.path.dirname(log_path), exist_ok=True)
    with open(log_path, 'a') as f:
        f.write(f"{datetime.now()} | {email} | {status}\n")

def send_email(to_email, subject, message):
    config = load_config()
    sender_email = config.get('email')
    sender_password = config.get('password')
    smtp_server = config.get('smtp_server', 'smtp.gmail.com')
    smtp_port = config.get('smtp_port', 587)

    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = to_email
    msg.set_content(message)

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)
        server.send_message(msg)
        server.quit()
        print(f"Email sent successfully to {to_email}")
        log_status(to_email, "Success")
    except Exception as e:
        print(f"Failed to send email to {to_email}: {e}")
        log_status(to_email, f"Failed: {e}")