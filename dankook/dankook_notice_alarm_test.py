# -*- coding: utf-8 -*-

########## 테스트 코드

import requests
from bs4 import BeautifulSoup
import os
import telegram
import sys
import time
import re

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

my_token = '봇 토큰'
my_chat_id = "채널 주소 / 서비스 채널은 '@***' / 테스트 채널은 '-***'"
req = requests.get('http://www.dankook.ac.kr/web/kor/-390')     # 단국대는 일반공지 - 천안 / 죽전 / 공통

client_errors = [400, 401, 403, 404, 408]
server_errors = [500,502, 503, 504]

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
all_posts_subject = soup.select('ul > li > div.subject > a')
all_posts_btm_area = soup.select('ul > li > div.btm_area > span.table_category')
num = soup.find_all(alt='상단공지')                 # 상단 공지 크롤링 / num에 리스트로 들어가니까 카운트 가능
save_url_messageld = []
save_messageld = []
use_url_messageld = []
use_messageld = []

CheonanCommonPosts = []
CheonanCommonArea = []

for i in range(len(num)):           # 공지로 위로 올라간 게시글 제외한 최신 게시글 분류
    del all_posts_subject[0]
    del all_posts_btm_area[0]

for i in range(len(all_posts_btm_area)):
    all_posts_btm_area[i] = all_posts_btm_area[i].text[8:10]    # 천안 / 죽전 / 공통 단어만 뽑아내기

for i, all_post_subject in enumerate(all_posts_subject):        # 뽑아낸 단어 인덱스를 기반으로
    if all_posts_btm_area[i] != "죽전":                           # 게시글 필터링
        CheonanCommonPosts.append(all_posts_subject[i])         # 원하는 데이터는 공통, 천안
        CheonanCommonArea.append(all_posts_btm_area[i])

for i, CheonanCommonPost in enumerate(CheonanCommonPosts):          # 원하는 데이터
    save_url_messageld.append(str(CheonanCommonPost).split('"')[1])       # _Bbs_WAR_bbsportlet_messageId=714769
    save_messageld.append(save_url_messageld[i].split('&amp')[9])   # 앞 뒤에 중복되는 문자열이 없다.
    use_url_messageld.append(str(CheonanCommonPost.get('href')))        # 그래서 a href 부분을 save_url_~ 리스트에 입력하고
    use_messageld.append(use_url_messageld[i].split('&')[9])    # &amp;로 다시 분리한다.
print(use_messageld)                                                                    # .get을 안쓴 이유는 CheonanCommonPosts가 리스트이기 때문.
print(save_messageld)
save_messageld[0] = save_messageld[0].lstrip(";")               # 파일 리스트로 불러올때 ; 기준으로 나누려고 0번 앞에 ;를 제거함

if not(os.path.isfile(os.path.join(BASE_DIR, 'dankook_latest.txt'))):
    new_file = open("dankook_latest.txt", 'w+',encoding='utf-8')
    new_file.writelines(save_messageld)
    new_file.close()

with open(os.path.join(BASE_DIR, 'dankook_latest.txt'), 'r+',encoding='utf-8') as f_read:    # DB 구현후 변경 에정
    before = f_read.readline().split(";")
    for i, CheonanCommonPost in enumerate(CheonanCommonPosts):                      # 기존 크롤링 한 부분과 최신 게시글 사이에 게시글이 존재하는지 확인
        print("post = " + CheonanCommonPost.text)
        print("new = " + use_messageld[i])
        print("before = " + before[0])         #
        if before[0] == use_messageld[i]:
            print("최신글입니다.")
            break
        elif before[1] == use_messageld[i]:
            print("두번째 게시글이랑 체크, 첫 게시글 삭제된거냐")
            break
        elif before[2] == use_messageld[i]:
            print("게시글 2개 삭제는 에바자나")
            break
        else:
            url = CheonanCommonPost.get('href')
            print(url)
            try:
                if CheonanCommonPost != CheonanCommonPosts[5]:       # 10번 post 이상 넘어가는지 확인 / 텔레그램 메시지가 url 10개 이상 한번에 못보냄
                    bot.sendMessage(chat_id=my_chat_id, text= CheonanCommonArea[i] + "공지 : " + CheonanCommonPost.text)
                    bot.sendMessage(chat_id=my_chat_id, text=url)
                else:
                    break
            except Exception as ex:
                print("timeout")            # 짧은 시간에 message를 과도하게 보내면 timeout이 뜨는것같다.
                break                       # message를 많이 보내서 발생한다기 보다는, 한번에 보낼 수 있는 url의 양이 10개로 제한되어 있는듯

with open(os.path.join(BASE_DIR, 'dankook_latest.txt'),'w+',encoding='utf-8') as f_write:
    f_write.writelines(save_messageld)

print("\n")