# 웹크롤링을 위한 모듈
from NaverNewsCrawler import NaverNewsCrawler
# 이메일 발송을 위한 모듈들
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
import re
# 엑셀 파일 읽기위한 모듈
from openpyxl import load_workbook

user_input = input('키워드를 입력하세요: ')

crawler = NaverNewsCrawler(user_input)

user_interset = input('엑셀 파일명을 입력하세요(파일명.xlsx): ')

crawler.get_news(user_interset)

SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 465
SMTP_USER = 'kshwbft@gmail.com'
SMTP_PASSWORD = ''


def send_mail(name, addr, subject, contents, attachment=None):
    if not re.match('(^[a-zA-Z0-9_.-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)', addr):
        print('Wrong email')
        return

    msg = MIMEMultipart('alternative')
    if attachment:
        msg = MIMEMultipart('mixed')

    msg['From'] = SMTP_USER
    msg['To'] = addr
    msg['Subject'] = name + '님, ' + subject

    text = MIMEText(contents, _charset='utf-8')
    msg.attach(text)

    if attachment:
        from email.mime.base import MIMEBase
        from email import encoders

        file_data = MIMEBase('application', 'octect-stream')
        file_data.set_payload(open(attachment, 'rb').read())
        encoders.encode_base64(file_data)

        import os
        filename = os.path.basename(attachment)
        file_data.add_header('Content-Disposition',
                             'attachment; filename="'+filename+'"')
        msg.attach(file_data)

    smtp = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)
    smtp.login(SMTP_USER, SMTP_PASSWORD)
    smtp.sendmail(SMTP_USER, addr, msg.as_string())
    smtp.close()


wb = load_workbook('email list_fastcampus news.xlsx')
data = wb.active
print(data)
