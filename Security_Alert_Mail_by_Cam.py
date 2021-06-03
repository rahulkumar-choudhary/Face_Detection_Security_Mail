import cv2

from datetime import date
from datetime import datetime

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

def Security_mail():
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
    
    
cap=cv2.VideoCapture(0)
model=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

while True:
    ret, photo=cap.read()
    faces=model.detectMultiScale(photo)
    if len(faces) ==0:
        pass
    else:
        for num_face in range(len(faces)):
            x1=faces[num_face][0]
            y1=faces[num_face][1]
            x2=x1+faces[num_face][2]
            y2=y1+faces[num_face][3]

            aphoto=cv2.rectangle(photo, (x1,y1),(x2,y2),[0,255,0],5)

            cphoto=photo[x1:x2, y1:y2]

        cv2.imshow('hi',aphoto)
        if cv2.waitKey(10)==13:
            break

Security_mail()

cv2.destroyAllWindows()
cap.release()
