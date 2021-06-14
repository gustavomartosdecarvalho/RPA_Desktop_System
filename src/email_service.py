from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
from email.message import EmailMessage
import smtplib
import os

class EmailService:

    def send_simple_email(self):
        try:
            print(' - [Email presentation only for TEST] ')
            # - - - - - - - - - - - -
            # > Script send to an simple Email
            # - - - - - - - - - - - -
            # msg = EmailMessage()
            # msg.set_content("Email content \n successfully")
            # msg['From'] = 'you@email.com'
            # msg['To'] = 'someone@email.com'
            # msg['Subject'] = ' Subject Email'
            # s = smtplib.SMTP('ServerNAME', 25)
            # s.send_message(msg)
            # s.quit()
            # return True
        except Exception as e:
            print(" - Error sending email: ", e)
            return False


    def send_html_email(self, evidence_path):
        try:
            print(' - [Email presentation only for TEST]: ', evidence_path)
            # - - - - - - - - - - - -
            # > Script send to an Email with html body
            # - - - - - - - - - - - -
            # Use SMT address
            # server = smtplib.SMTP('SMTPADDRESS', 25)
            # server.ehlo()
            # obj_msg = MIMEMultipart()
            # obj_msg['From'] = 'you@email.com'
            # obj_msg['To'] = 'someone@email.com'
            # obj_msg['Subject'] = ' Subject Email'
            # # To put a image, need src and the link
            # message = '<html><body><p>Ola, <b>Email de teste</p></body></html>'
            # obj_msg.attach(MIMEText(message, 'html', 'utf-8'))
            # server.send_message(obj_msg)
            # server.close()
            # return True
        except Exception as e:
            print(" - Error sending email: ", e)
            return False