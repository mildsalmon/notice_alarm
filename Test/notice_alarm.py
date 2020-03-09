# -*- coding: utf-8 -*-

###### 테스트 코드

import security_data
import requests
import sys
import telegram
from bs4 import BeautifulSoup
import os
import name_list


security_data_set_server_name = name_list.name_list_security()
name_list_notice_type = name_list.name_list_notice_type()

class NoticeAlarm:
    def __init__(self, univ_name, notice_type, url):
        self.BASE_DIR = os.path.dirname(os.path.abspath(__file__))

        bot_token = security_data.bot_info(security_data_set_server_name[0])

        self.create_telegram_bot(bot_token)
        self.univ_name = univ_name
        self.notice_type = notice_type
        self.url = url

        # if univ_name == "한라":
        #
        # elif univ_name == "단국":
        txt_mid_name = ''
        for i, name in enumerate(name_list_notice_type):
            if name == notice_type:
                txt_mid_name = str(i)
        self.save_file_name = univ_name + "_" + txt_mid_name + "_old_data.txt"
        # self.__web_errors(req.status_code)
        # save_content, posts, user_boardSeq = self.html_analyze(req, univ_name)
        # if not(os.path.isfile(os.path.join(BASE_DIR, save_file_name))):
        #     self.write_file(BASE_DIR, save_file_name, save_content)
        # self.matching(BASE_DIR, save_file_name, posts, user_boardSeq, univ_name, bot, chat_id, notice_type)
        # self.write_file(BASE_DIR, save_file_name, save_content)

    # 웹의 상태 코드를 받아서 클라이언트 에러 / 서버 에러가 발생시 프로그램 종료
    # 공통 요소라 부모 클래스
    def web_errors(self, status_code_req):
        client_errors = [400, 401, 403, 404, 408]
        server_errors = [500, 502, 503, 504]
        status_errors = client_errors + server_errors

        if status_code_req in status_errors:
            if status_code_req in client_errors:
                print(str(status_code_req) + ": 클라이언트 에러")
            elif status_code_req in server_errors:
                print(str(status_code_req) + ": 서버 에러")
            sys.exit(1)
        print("a")

    def show_chat_id(self):
        chat_id = security_data.chat_info(security_data_set_server_name[0])
        return chat_id

    # 공통 요소이긴 하지만 텔레그램 끼리 클래스 분리
    # 텔레그램 봇 생성
    def create_telegram_bot(self, bot_token):
        self.bot = telegram.Bot(token=bot_token)

    # 텔레그램 봇 메시지 전송
    def telegram_bot_sendmessage(self, chat_id, new_post):
        self.bot.sendMessage(chat_id=chat_id, text=self.notice_type + "공지 : " + new_post)
        self.bot.sendMessage(chat_id=chat_id, text=self.url)


    # 공통
    # 파일 쓰기, 최신 데이터로
    def write_file(self, save_content):
        with open(os.path.join(self.BASE_DIR, self.save_file_name),'w+', encoding='utf-8') as f_write:
            f_write.writelines(save_content)

    # 공통
    # 파일 읽기
    def open_file(self):
        with open(os.path.join(self.BASE_DIR, self.save_file_name),'r+', encoding='utf-8') as f_read:
            old_data = f_read.readline().split(";")
        return old_data

    # 공통
    # url은 학교별 html 분석에서 끝내고 오기 .get('href') 전까지
    def matching(self, posts, use_boardSeq, chat_id):
        old_data = self.open_file()
        for index, post in enumerate(posts):
            print("post title = " + post.text)
            print("new post Seq = ", use_boardSeq[index])
            print("old data Seq num1 = ", old_data[0])
            if old_data[0] == use_boardSeq[index]:
                print("최신글")
                break
            elif old_data[1] == use_boardSeq[index]:
                print("두번째 게시글이랑 체크")
                break
            elif old_data[2] == use_boardSeq[index]:
                print("세번째 게시글 체크")
                break
            else:
                url = self.url + post.get('href')
                print(url)
                try:
                    if post != posts[5]:
                        print('a')
                        self.telegram_bot_sendmessage(chat_id=chat_id, new_post=post.text)
                    else:
                        break
                except Exception as ex:
                    print(ex)
                    break