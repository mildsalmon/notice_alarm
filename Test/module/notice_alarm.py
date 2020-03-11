# -*- coding: utf-8 -*-

###### 테스트 코드

from security.security_data import *
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from telegram_bot.telegram_bot_control import TelegramBot


class NoticeAlarm:
    def __init__(self, re_univ_name, re_notice_type):
        # univ_name = {'한라': 'halla',
        #              '단국': 'dankook',
        #              'test': 'test'}
        # notice_type = {'일반': 'normal',
        #                '학사': 'academic',
        #                '죽전': 'jukjeon',
        #                '천안': 'cheonan',
        #                '공통': 'common'}
        self.BASE_DIR = os.path.join(os.path.dirname(os.path.abspath(os.path.dirname(__file__))),"data_file")
        self.univ_name = re_univ_name
        self.re_notice_type = re_notice_type
        # self.url = url
        self.file_name = self.univ_name + "_" + self.re_notice_type + "_old_data.txt"

    def web_errors(self, status_code_req):
        client_errors = [400, 401, 403, 404, 408]
        server_errors = [500, 502, 503, 504]
        status_errors = client_errors + server_errors

        if status_code_req in status_errors:
            if status_code_req in client_errors:
                print(str(status_code_req) + ": 클라이언트 에러")
                return False
            elif status_code_req in server_errors:
                print(str(status_code_req) + ": 서버 에러")
                return False
        else:
            return True

    def exit(self):
        sys.exit(1)

    def show_chat_id(self):
        chat_id = chat_info(receive_chat_name=self.univ_name)
        return chat_id

    # 공통
    # 파일 쓰기, 최신 데이터로
    def write_file(self, save_content):
        with open(os.path.join(self.BASE_DIR, self.file_name),'w+', encoding='utf-8') as f_write:
            f_write.writelines(save_content)

    # 공통
    # 파일 읽기
    def open_file(self):
        with open(os.path.join(self.BASE_DIR, self.file_name),'r+', encoding='utf-8') as f_read:
            old_data = f_read.readline().split(";")
        return old_data

    # 공통
    # url은 학교별 html 분석에서 끝내고 오기 .get('href') 전까지
    def matching(self, posts, use_boardSeq, chat_id, re_url=""):
        telegram_bot = TelegramBot(re_univ_name=self.univ_name, re_notice_type=self.re_notice_type)
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
                url = re_url + post.get('href')
                print(url)
                try:
                    if post != posts[5]:
                        telegram_bot.telegram_bot_sendmessage(chat_id=chat_id, new_post=post.text, url=url)
                    else:
                        break
                except Exception as ex:
                    print(ex)
                    break