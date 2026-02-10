import smtplib
from email.message import EmailMessage
from secrets import sender_email,password


def send_email(reciever_email: str, subject: str, content: str) -> str:
    """Send an email to the given receiver email address with the specified subject and content."""
    msg = EmailMessage()
    msg["From"] = sender_email
    msg["To"] = reciever_email
    msg["Subject"] = subject
    msg.set_content(content)

    # Connect to Gmail Server
    with smtplib.SMTP_SSL('smtp.gmail.com',465) as server:
        server.login(sender_email,password)
        server.send_message(msg)

    print("Email sent successfully")
    return "Email sent successfully"

if __name__ == "__main__":
    send_email("4mh23cs179@gmail.com", subject="Hello from python",content="this is a test emailfrom python")