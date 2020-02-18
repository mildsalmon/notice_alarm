import requests
from bs4 import BeautifulSoup
import os
import telegram
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

my_token = '****'
req = requests.get('http://www.halla.ac.kr/mbs/kr/jsp/board/list.jsp?boardId=23401&mcategoryId=&id=kr_060101000000')
my_chat_id = "****"

client_errors = [400, 401, 403, 404, 408]
server_errors = [500, 502, 503, 504]

if req.status_code in client_errors:
    sys.exit(1)
elif req.status_code in server_errors:
    sys.exit(1)

bot = telegram.Bot(token=my_token)
html = req.text
soup = BeautifulSoup(html, 'html.parser')
posts = soup.select('table > tbody > tr > td > a')
count_page_num = 0
count_notice_num = 0

for post in posts:
    post_href = post.get('href')
    if 'mcategoryId' in post_href:
        count_notice_num = count_page_num
        break
    count_page_num = count_page_num + 1

for i in range(count_notice_num):  # 공지로 위로 올라간 게시글 제외한 최신 게시글 분류
    del posts[0]

with open(os.path.join(BASE_DIR, 'latest.txt'), 'r+') as f_read:  # DB 구현후 변경 에정
    before = f_read.readline()

    for post in posts:  # 기존 크롤링 한 부분과 최신 게시글 사이에 게시글이 존재하는지 확인
        if before == post.text:
            print("최신글입니다.")
            break
        elif before != post:
            url = "http://www.halla.ac.kr/mbs/kr/jsp/board/" + post.get('href')
            print(url)
            bot.sendMessage(chat_id=my_chat_id, text="새 공지사항이 있습니다.")
            bot.sendMessage(chat_id=my_chat_id, text=post.text)
            bot.sendMessage(chat_id=my_chat_id, text=url)

            with open(os.path.join(BASE_DIR, 'latest.txt'), 'w+') as f_write:
                f_write.write(post.text)

            # f_write.close()
    # f_read.close()