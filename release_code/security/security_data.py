# -*- coding: utf-8 -*-


##### 보안 처리되어야 하는 값을 처리.
#   차후 값은 파일에 보관하고, 파일에서 읽어오는 형식으로 변경 예정

import os

# 학교별로 / 학교에서도 테스트, 서비스별로 다른 봇을 사용한다.
server_name = {'test' : 'test',
               'halla_service' : 'halla',
               'dankook_serivce' : 'dankook'}

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def open_file(kind):
    if kind == "token":
        with open(os.path.join(BASE_DIR, "token.txt"), 'r+', encoding='utf-8') as f_read:
            token = f_read.readline().split(";")
            return token
    elif kind == "chat":
        with open(os.path.join(BASE_DIR, "chat.txt"), 'r+', encoding='utf-8') as f_read:
            chat = f_read.readline().split(';')
            return chat

def bot_info(receive_bot_name):
    token = open_file(kind="token")
    if receive_bot_name == server_name['test']:
        test_bot_token = token[0]
        return test_bot_token
    elif receive_bot_name == server_name['halla_service']:
        halla_service_bot_token = token[1]
        return halla_service_bot_token
    elif receive_bot_name == server_name['dankook_serivce']:
        dankook_service_bot_token = token[2]
        return dankook_service_bot_token

# 학교별 -> 테스트, 서비스별로 다른 채팅을 사용한다.
# 테스트 채팅 id는 -로, 서비스 채팅 id는 @로 시작한다.
def chat_info(receive_chat_name):
    chat = open_file(kind="chat")
    if receive_chat_name == server_name['test']:
        test_chat_id = chat[0]
        return test_chat_id
    elif receive_chat_name == server_name['halla_service']:
        halla_service_chat_id = chat[1]
        return halla_service_chat_id
    elif receive_chat_name == server_name['dankook_serivce']:
        dankook_service_chat_id = chat[2]
        return dankook_service_chat_id

if __name__ == "__main__":
    print(BASE_DIR)
    print(open_file(kind="token"))
    print(bot_info('halla'))
    print(chat_info('test'))