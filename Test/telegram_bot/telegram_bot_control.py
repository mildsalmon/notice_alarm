import telegram
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from security.security_data import *

# 공통 요소이긴 하지만 텔레그램 끼리 클래스 분리
# 텔레그램 봇 생성
class TelegramBot:
    def __init__(self, re_univ_name, re_notice_type):
        # univ_name = {'한라': 'halla',
        #              '단국': 'dankook',
        #              'test': 'test'}
        # notice_type = {'일반': 'normal',
        #                '학사': 'academic',
        #                '죽전': 'jukjeon',
        #                '천안': 'cheonan',
        #                '공통': 'common'}

        self.bot_token = bot_info(re_univ_name)
        self.univ_name = re_univ_name
        self.notice_type = re_notice_type
        self.create_telegram_bot()

    def create_telegram_bot(self):
        self.bot = telegram.Bot(token=self.bot_token)

    # 텔레그램 봇 메시지 전송
    def telegram_bot_sendmessage(self, chat_id, new_post, url):
        self.bot.sendMessage(chat_id=chat_id, text=self.notice_type + "공지 : " + new_post)
        self.bot.sendMessage(chat_id=chat_id, text=url)