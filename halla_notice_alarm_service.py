# -*- coding: utf-8 -*-

########## 서비스 코드

import requests
from bs4 import BeautifulSoup
import os
import telegram
import sys
import time

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

my_token = '봇 토큰'
my_chat_id = "채널 주소 / 서비스 채널은 '@***' / 테스트 채널은 '-***'"
req = requests.get('http://www.halla.ac.kr/mbs/kr/jsp/board/list.jsp?boardId=23401&mcategoryId=&id=kr_060101000000')
# 일반 = boardId = 23401
client_errors = [400, 401, 403, 404, 408]
server_errors = [500, 502, 503, 504]

print(time.strftime("%c", time.localtime(time.time())))

if req.status_code in client_errors:
    print(req.status_code + ": 클라이언트 에러")
    sys.exit(1)
elif req.status_code in server_errors:
    print(req.status_code + ": 서버 에러")
    sys.exit(1)

bot = telegram.Bot(token=my_token)
html = req.text
soup = BeautifulSoup(html, 'html.parser')
posts = soup.select('td > a')
num = soup.find_all(title='공지')
save_boardSeq = []
use_boardSeq = []

for i in range(len(num)):  # 공지로 위로 올라간 게시글 제외한 최신 게시글 분류
    del posts[0]

for post in posts:
    save_boardSeq.append(str(post).split("&amp")[2])  # 가장 최신 공지랑 같은지 검사
    use_boardSeq.append(str(post).split("&amp;")[2])

save_boardSeq[0] = save_boardSeq[0].lstrip(";")

if not (os.path.isfile(os.path.join(BASE_DIR, 'latest.txt'))):
    new_file = open("latest.txt", 'w+', encoding='utf-8')
    new_file.writelines(save_boardSeq)
    new_file.close()

with open(os.path.join(BASE_DIR, 'latest.txt'), 'r+', encoding='utf-8') as f_read:  # DB 구현후 변경 에정
    before = f_read.readline().split(";")
    for i, post in enumerate(posts):  # 기존 크롤링 한 부분과 최신 게시글 사이에 게시글이 존재하는지 확인
        print("post = " + post.text)
        print("new = " + use_boardSeq[i])
        print("before = " + before[0])  #
        if before[0] == use_boardSeq[i]:
            print("최신글입니다.")
            break
        elif before[1] == use_boardSeq[i]:
            print("두번째 게시글이랑 체크, 첫 게시글 삭제된거냐")
            break
        elif before[2] == use_boardSeq[i]:
            print("게시글 2개 삭제는 에바자나")
            break
        else:
            url = "http://www.halla.ac.kr/mbs/kr/jsp/board/" + post.get('href')
            print(url)
            try:
                if post != posts[5]:  # 10번 post 이상 넘어가는지 확인 / 텔레그램 메시지가 url 10개 이상 한번에 못보냄
                    bot.sendMessage(chat_id=my_chat_id, text="일반공지 : " + post.text)
                    bot.sendMessage(chat_id=my_chat_id, text=url)
                else:
                    break
            except Exception as ex:
                print("timeout")  # 짧은 시간에 message를 과도하게 보내면 timeout이 뜨는것같다.
                break  # message를 많이 보내서 발생한다기 보다는, 한번에 보낼 수 있는 url의 양이 10개로 제한되어 있는듯

with open(os.path.join(BASE_DIR, 'latest.txt'), 'w+', encoding='utf-8') as f_write:
    f_write.writelines(save_boardSeq)

print("\n")