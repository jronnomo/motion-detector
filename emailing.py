import os
import dotenv
import smtplib
from email.message import EmailMessage
import imghdr

dotenv.load_dotenv()
PASSWORD = os.getenv("PASSWORD")
SENDER = os.getenv("USERNAME")
RECEIVER = 'ggronnii@gmail.com'


def send_email(image_path):
    email_message = EmailMessage()
    email_message["Subject"] = "New customer showed up!"
    email_message.set_content("New customer showed up!")
    with open(image_path, "rb") as file:
        content = file.read()
    email_message.add_attachment(content, maintype="image", subtype=imghdr.what(None, content))

    gmail = smtplib.SMTP('smtp.gmail.com', 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(SENDER, PASSWORD)
    gmail.sendmail(SENDER, RECEIVER, email_message.as_string())
    gmail.quit()


if __name__ == "__main__":
    send_email('./images/1.png')
