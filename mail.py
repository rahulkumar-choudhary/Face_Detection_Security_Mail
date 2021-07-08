#Enter user mail ID in variable email_user
#Enter reciever mail ID in variable email_send
#Enter password of the user mail ID in email_user_pass

#smtplib to send email
import smtplib
#MIMEText for plain text
from email.mime.text import MIMEText
#MIMEMultipart for multipart form request
from email.mime.multipart import MIMEMultipart
#Base class MIMEBase
from email.mime.base import MIMEBase
from email import encoders

from datetime import date
from datetime import datetime

now = datetime.now()
today = date.today()

def securityMail():
    email_user='user@mail.com'
    email_send='reciver@mail.com'
    email_user_pass='PASSWORDXXXXXXXXXXXXXX'

    subject= '⚠ Security Alert!! ⚠'
    #Multipart message as we have image and text both
    msg=MIMEMultipart()
    #Headers
    msg['From']=email_user
    msg['To']=email_send
    msg['Subject']=subject

    dtime= now.strftime("%H:%M:%S")
    ddate=today.strftime("%B %d, %Y")
    #Body of email
    body = '''
⚠ Security Alert! ⚠
Someone has been spotted in the camara.

During:-
Date: '''+ddate+'''
Time: '''+dtime+'''

Front face of the person in jpg format:

'''
    #Adding text to multipart 
    msg.attach(MIMEText(body,'plain'))
    #Open the image
    filename='image.jpg'
    attachment =open(filename, 'rb')

    part = MIMEBase('application', 'octet-stream')
    #Attaching the content
    part.set_payload((attachment).read())
    #Enclode image in base64 string
    encoders.encode_base64(part)
    #Content-Disposition to indicate if content will be visisble or downloadable. In this case downloadable, as attachment option is selected
    part.add_header('Content-Disposition', "attachment; filename="+filename)
    
    #Attaching the image to message
    msg.attach(part)
    #Covert into string
    text= msg.as_string()
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(email_user,email_user_pass)

    server.sendmail(email_user,email_send,text)
    server.quit()
