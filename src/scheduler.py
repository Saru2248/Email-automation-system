import schedule
import time
from datetime import datetime
from email_sender import send_email
from utils import load_email_data

def schedule_emails():
    data = load_email_data()

    for row in data:
        email = row['email']
        subject = row['subject']
        message = row['message']
        schedule_time = row['schedule_time']

        schedule.every().day.at(
            datetime.strptime(schedule_time, "%Y-%m-%d %H:%M").strftime("%H:%M")
        ).do(send_email, email, subject, message)

def run_scheduler():
    schedule_emails()
    print("Scheduler started...")

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == '__main__':
    run_scheduler()