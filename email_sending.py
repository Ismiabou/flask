from email.mime.text import MIMEText
import smtplib

thanking = "Thank you for the feedback"


def send_email(email, thanking_):
    from_email = "ismailabou6@gmail.com"
    from_password = "123688mr"
    to_email = email

    subject = "Feedback"
    message = thanking_

    msg = MIMEText(message, 'html')
    msg['Subject'] = subject
    msg['To'] = to_email
    msg['From'] = from_email

    gmail = smtplib.SMTP('smtp.gmail.com', 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email, from_password)
    gmail.send_message(msg)
