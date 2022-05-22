import smtplib
import ssl
from email.message import EmailMessage

sender_email = input("Enter sender email: ")
receiver_email = input("Enter receiver email: ")
subject = input("Enter subject: ")
body = input("Enter body: ")
user_password = input("Enter password: ")

message = EmailMessage()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
message.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, user_password)
    server.sendmail(sender_email, receiver_email, message.as_string())