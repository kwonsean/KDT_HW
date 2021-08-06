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
        with open(attachment, 'rb') as file:
            file_data.set_payload(file.read())
        encoders.encode_base64(file_data)

        file_data.add_header('Content-Disposition',
                             "attachment", filename=attachment)
        msg.attach(file_data)

    smtp = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)
    smtp.login(SMTP_USER, SMTP_PASSWORD)
    smtp.sendmail(SMTP_USER, addr, msg.as_string())
    smtp.close()


wb = load_workbook('email list_fastcampus news.xlsx')
data = wb.active
# 이름과 이메일이 지정된 곳을 범위로 지정
area = data['B3:C4']
# 한줄 한줄 내용을 임시로 저장할 빈 리스트 선언
list = []
# 2개의 for문을 이용하여 B3-B4-C3-C4 순서로 cell이 조회되도록 함
# 이때 cell의 value값을 list에 넣는다.
for row in area:
    for cell in row:
        list.append(cell.value)
        # list의 길이가 2가 되면 즉, 리스트에 이름과 이메일이 하나씩 들어가면 각 값을 name과 addr 변수에 넣어준다.
        if len(list) == 2:
            name = list[0]
            addr = list[1]
            # 이후 리스트는 다시 빈 리스트로 초기화를 한다.
            list = []
            # 앞서 user가 입력한 키워드를 중심으로 제목과 내용을 작성한다.
            title = user_input+'에 관한 내용 정리해서 보내드립니다.'
            contents = user_input+'에 관한 뉴스 기사 모음 파일입니다.'
            send_mail(name, addr, title, contents, user_interset)
            print('전송 성공')
