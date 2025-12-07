import smtplib
from email.message import EmailMessage

def send_email(smtp_host, smtp_port, username, password, to, subject, body):
    msg = EmailMessage()
    msg["From"] = username
    msg["To"] = to
    msg["Subject"] = subject
    msg.set_content(body)
    with smtplib.SMTP(smtp_host, smtp_port) as s:
        s.starttls()
        s.login(username, password)
        s.send_message(msg)
    return True

if __name__ == "__main__":
    print("This is a template. Fill credentials to send email.")