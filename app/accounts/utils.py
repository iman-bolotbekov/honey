from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import ssl
import smtplib
import os
from platform import python_version

email_sender = 'tt6824193@gmail.com'
email_password = 'juynwtnytlyjlamh'

yandex_sender = 'ty6824193@yandex.ru'
yandex_password = 'testTESTtest123'

mail_sender = 'ty6824193@mail.ru'
mail_password = 'Lbf406DZxRz61xEhfWWx'


def send_email(sender, password, receiver, subject, body):
    if 'yandex' in receiver:
        msg = MIMEMultipart()
        msg['From'] = sender
        msg['To'] = receiver
        msg['Subject'] = subject
        msg.attach(
            MIMEText(body, 'plain')
        )
        server = smtplib.SMTP_SSL('smtp.yandex.ru', 465)
        server.ehlo(sender)
        server.login(sender, password)
        server.auth_plain()
        server.send_message(f'\t\t\t\t\t\t\t\t\t\t{subject}\n{msg}')
        server.quit()
        return str(body)
    if 'gmail' in receiver:
        context = ssl.create_default_context()
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.ehlo()  # Can be omitted
            server.starttls(context=context)
            server.ehlo()  # Can be omitted
            server.login(sender, password)
            server.sendmail(sender, receiver, f'\t\t\t\t\t\t\t\t\t\t{subject}\n{body}')
        return str(body)


def send_mail(sender, password, receiver, subject, body):
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = 'Sender <' + sender + '>'
    msg['To'] = receiver
    msg['Reply-To'] = sender
    msg['Return-Path'] = sender
    msg['X-Mailer'] = 'Python/' + (python_version())
    part_text = MIMEText(f'\t\t\t\t\t\t\t\t\t\t{subject}\n{body}', 'plain')
    msg.attach(part_text)
    mail = smtplib.SMTP_SSL('smtp.mail.ru')
    mail.login(sender, password)
    mail.sendmail(sender, receiver, msg.as_string())
    mail.quit()
    return body