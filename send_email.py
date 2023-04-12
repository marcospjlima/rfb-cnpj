
import os
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

smtp_server = os.environ.get("SMTP_HOST")
smtp_port = os.environ.get("SMTP_PORT")
smtp_username = os.environ.get("EMAIL_FROM")
smtp_password = os.environ.get("PASSWORD")
sender = os.environ.get("EMAIL_FROM")
recipient = os.environ.get("EMAIL_TO")
cc = os.environ.get("EMAIL_CC")

def enviar_email(assunto, mensagem):

    # Cria a mensagem de e-mail
    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = recipient
    msg['Cc'] = cc
    msg['Subject'] =mensagem
    body =  assunto
    msg.attach(MIMEText(body, 'plain'))

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, smtp_port, context=context) as server:
        server.login(smtp_username, smtp_password)
        recipients = [recipient] + [cc] if cc else []
        server.sendmail(sender, recipients, msg.as_string())

