#Enter user mail ID in variable email_user
#Enter reciever mail ID in variable email_send
#Enter password of the user mail ID in email_user_pass

import cv2
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

from datetime import date
from datetime import datetime


def securityMail():
    cv2.imwrite("image.jpg", cphoto)

    email_user='user@mail.com'
    email_send='reciver@mail.com'
    email_user_pass='PASSWORDXXXXXXXXXXXXXX'

    subject= '⚠ Security Alert!! ⚠'

    current_time=datetime.datetime.now()

    msg=MIMEMultipart()
    msg['From']=email_user
    msg['To']=email_send
    msg['Subject']=subject

    today = date.today()

    dtime= now.strftime("%H:%M:%S")
    ddate=today.strftime("%B %d, %Y")

    body = '''
    ⚠ Security Alert! ⚠
    Someone has been spotted in the camara.

    During:-
    Date: '''+ddate+'''
    Time: '''+dtime

    msg.attach(MIMEText(body,'plain'))

    filename='image.jpg'
    attachment =open(filename, 'rb')

    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename="+filename)

    msg.attach(part)
    text= msg.as_string()
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(email_user,email_user_pass)

    server.sendmail(email_user,email_send,text)
    server.quit()
