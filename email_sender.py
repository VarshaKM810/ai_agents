import smtplib
from email.mime.text import MIMEText


sender = "varshakm302@gmail.com"
receiver = "4mh23cs179@gmail.com"
password = "dhej otyw hjsw vgrc"


msg = MIMEText("Hello! This mail is sent using Python.")
msg["Subject"] = "Python Email Test"
msg["From"] = sender
msg["To"] = receiver

# Connect to Gmail Server
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(sender, password)

server.sendmail(sender, receiver, msg.as_string())
server.quit()

print("Email sent successfully")
