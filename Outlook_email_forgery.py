#coding:utf-8
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
import time

my_sender=''    # Sender email account 你的邮箱地址
my_pass = ''              # SMTP password 
my_user=''      # Recipient email account 对方邮箱

def mail(mail_name,i):
    ret=True
    mail_text = '''Just hacker'''
    try:
        msg=MIMEText(mail_text,'html','utf8')
        msg['From']=formataddr([mail_name,my_sender])
        # mail_name represents the sender’s nickname my_sender represents the sender’s email address
        msg['To']=formataddr(["just hacker",my_user])              # The corresponding recipient's email nickname and recipient's email account in brackets
        msg['Subject']="邮件主题-测试(mail_test)"

        server=smtplib.SMTP_SSL("smtp.xx.com", 465)  # SMTP server and port
        server.login(my_sender, my_pass)  # Corresponding to the sender's email account and SMTP password in brackets
        server.sendmail(my_sender,[my_user,],msg.as_string())  # Corresponding to the sender's email account, recipient's email account, and sending mail in brackets
        server.quit()
    except Exception:
        ret=False
    return ret

for i in range(1):
    # Sender's nickname with special characters inserted
    mail_name = '''admin <admin@outlook.com>　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　···'''
    ret=mail(mail_name,i)
    if ret:
        print("YES")
    else:
        print("No")
    time.sleep(1)