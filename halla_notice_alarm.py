import requests
from bs4 import BeautifulSoup
import os
import telegram

my_token = '964838878:AAHq2EX0j70vQSGEuCz2mryIRdmQ-UxK_gA'
bot = telegram.Bot(token=my_token)
# chat_id = bot.getUpdates()[-1].message.chat.id
my_chat_id = "@mildsalmon"
# updates = bot.getUpdates()

# for u in updates:
#     print(u.message)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
while True:
    req = requests.get('http://www.halla.ac.kr/mbs/kr/jsp/board/list.jsp?boardId=23401&mcategoryId=&id=kr_060101000000')
    req.encoding = 'utf-8'

    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    posts = soup.select('table > tbody > tr > td > a')

    count_page_num = 0
    count_notice_num = 0

    for i in posts:
        # print(i.text)
        # print(i.get('href'))
        # print(count_page_num)
        category = i.get('href')
        count_page_num = count_page_num + 1  # 공지 제목 다음을 카운트하기 위해
        if 'mcategoryI' not in category:
            count_notice_num = count_page_num
    # print(posts)

    latest = posts[count_notice_num].text
    latest_category = posts[count_notice_num].get('href')

    # custom_keyboard ={"keyboard":[["A","B"],["C","D"]]} #{"keyboard" : [["Done", "Done 3"], ["Update"], ["Log Time"]]}
    # reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
    # # reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
    # # bot.send_message(chat_id='@su_soo', text="Custom Keyboard Test", reply_markup=reply_markup)
    # bot.sendMessage(chat_id=chat_id, text='gk', reply_markup=custom_keyboard)
    with open(os.path.join(BASE_DIR, 'latest.txt'), 'r+') as f_read:
        before = f_read.readline()
        if before != latest:
            # bot.sendMessage(chat_id=chat_id, text='new')

            boardSeq = latest_category.find('boardSeq=')
            boardSeq_number = latest_category[boardSeq + 9:]

            url = "http://www.halla.ac.kr/mbs/kr/jsp/board/view.jsp?spage=1&boardId=23401&boardSeq=" + boardSeq_number + "&mcategoryId=&id=kr_060101000000&column=&search="

            bot.sendMessage(chat_id=my_chat_id, text="새 공지사항이 있습니다.")
            bot.sendMessage(chat_id=my_chat_id, text=latest)
            bot.sendMessage(chat_id=my_chat_id, text=url)
            with open(os.path.join(BASE_DIR, 'latest.txt'), 'w+') as f_write:
                f_write.write(latest)
                f_write.close()
        # else:
        #     # bot.sendMessage(chat_id=chat_id,text='x')
        #     bot.sendMessage(chat_id='@su_soo', text="새 공지 없음")
        f_read.close()



 # print(count_notice_num)ㅇㅁ