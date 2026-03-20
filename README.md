di# 📧 Email Automation & Reminder System

## 🚀 Overview

The **Email Automation & Reminder System** is a Python-based application designed to automate email communication and scheduling tasks. It eliminates repetitive manual work by allowing users to send emails automatically based on predefined schedules and data sources.

This project demonstrates real-world automation concepts used in industries such as HR, marketing, education, and operations.

---

## 🎯 Key Features

* 📤 Send automated emails using SMTP (Gmail supported)
* 📊 Read recipient data from CSV/Excel files
* ⏰ Schedule emails for specific date and time
* 🔁 Set up daily reminder emails
* ⚠️ Error handling for invalid emails and connection issues
* 📝 Logging system to track email status (Success/Failure)
* ⚙️ Config-based setup (secure and flexible)

---

## 🏗️ Project Structure

```
email-automation-system/
│
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── email_sender.py
│   ├── scheduler.py
│   ├── utils.py
│
├── data/
│   └── emails.csv
│
├── logs/                     # Auto-created logs directory
│
├── config/
│   └── config.example.json   # Sample config (no real credentials)
│
├── .gitignore
├── requirements.txt
├── README.md
```

---

## 🛠️ Tech Stack

* Python
* smtplib (Email sending)
* pandas (Data handling)
* schedule (Task scheduling)
* datetime (Time handling)

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/email-automation-system.git
cd email-automation-system
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

Activate it:

**Windows**

```bash
venv\Scripts\activate
```

**Mac/Linux**

```bash
source venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Configure Email Credentials

Create a new file:

```
config/config.json
```

Copy content from `config.example.json` and add your credentials:

```json
{
  "email": "your_email@gmail.com",
  "password": "your_app_password",
  "smtp_server": "smtp.gmail.com",
  "smtp_port": 587
}
```

⚠️ Use **App Password** (not your Gmail password)

---

### 5️⃣ Prepare Email Data

Edit:

```
data/emails.csv
```

Example:

```csv
email,subject,message,schedule_time
test@gmail.com,Meeting Reminder,Don't forget meeting at 5 PM,2026-03-21 17:00
```

---

## ▶️ How to Run

```bash
python src/main.py
```

You will see:

```
Starting Email Automation System...
Scheduler started...
```

---

## 📄 Logs (Output Example)

Logs are automatically generated in:

```
logs/email_logs.txt
```

Example:

```
2026-03-21 17:00:01 | test@gmail.com | SUCCESS
2026-03-21 17:05:10 | abc@gmail.com | FAILED: Invalid email
```

---

## 🧠 How It Works

1. 📂 Reads email data from CSV using pandas
2. ⏰ Scheduler checks for matching time
3. 📤 Sends email using SMTP protocol
4. 📝 Logs success or failure
5. 🔁 Repeats continuously

---

## 🌍 Real-World Use Cases

* HR interview reminders
* College/University notifications
* Marketing email campaigns
* Subscription/payment reminders
* Internal team alerts

---

## ⚠️ Limitations (Current Version)

* Uses CSV instead of database
* Basic scheduling (no timezone handling)
* No UI/dashboard
* Limited email validation

---

## 🚀 Future Improvements

* 📦 Database integration (SQLite/PostgreSQL)
* 🌐 Web dashboard (Flask/Django)
* 📧 HTML email templates
* 🔁 Retry mechanism for failed emails
* 🔐 Environment variable-based config
* 📊 Analytics dashboard

---

## 🤝 Contribution

Pull requests are welcome. For major changes, open an issue first to discuss improvements.

---

## 📌 Author

**Sarthak Dhumal**

---

## ⭐ If you found this useful

Give this repo a star ⭐ — it helps others discover it!
