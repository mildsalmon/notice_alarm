from module.notice_alarm import NoticeAlarm
import requests
from bs4 import BeautifulSoup
import os


class Dankook(NoticeAlarm):
    def __init__(self, re_notice_type, re_univ_name='dankook'):
        BASE_DIR = os.path.join(os.path.dirname(os.path.abspath(os.path.dirname(__file__))), "data_file")

        self.notice_type = {'죽전': 'jukjeon',
                            '천안': 'cheonan',
                            '공통': 'common'}
        self.reverse_notice = {'jukjeon':'죽전',
                               'cheonan':'천안',
                               'common':'공통'}
        url = ""

        super().__init__(re_univ_name=re_univ_name, re_notice_type=re_notice_type)

        self.req = requests.get("http://www.dankook.ac.kr/web/kor/-390")

        if not(self.web_errors(status_code_req=self.req.status_code)):
            self.exit()

        save_boardSeq, posts, use_boardSeq = self.html_analyze(notice_type=re_notice_type)

        if not (os.path.isfile(os.path.join(BASE_DIR, self.file_name))):
            self.write_file(save_content=save_boardSeq)

        old_data = self.open_file()
        self.matching(posts=posts, use_boardSeq=use_boardSeq, chat_id=self.show_chat_id())
        self.write_file(save_content=save_boardSeq)


    def html_analyze(self, notice_type):
        html = self.req.text
        soup = BeautifulSoup(html, 'html.parser')
        subjects = soup.select('ul > li > div.subject > a')
        btm_area = soup.select('ul > li > div.btm_area > span.table_category')
        notice_num = len(soup.find_all(alt='상단공지'))  # 새로운 게시글이 아닌 공지 글 개수를 카운트
        save_boardSeq = []
        use_boardSeq = []
        save_temp = []
        use_temp = []
        posts = []

        for i in range(notice_num):  # 게시글을 제외한 공지 글 제거
            del subjects[0]
            del btm_area[0]

        for i in range(len(btm_area)):
            btm_area[i] = btm_area[i].text[-3:-1]

        for i, subject in enumerate(subjects):
            if btm_area[i] == self.reverse_notice[notice_type]:
                posts.append(subjects[i])

        for i, post in enumerate(posts):
            save_temp.append(str(post).split('"')[1])
            save_boardSeq.append(save_temp[i].split('&amp')[9])
            use_temp.append(str(post).split('"')[1])
            use_boardSeq.append(use_temp[i].split('&amp;')[9])

        save_boardSeq[0] = save_boardSeq[0].lstrip(";")
        print(save_boardSeq)
        return save_boardSeq, posts, use_boardSeq


if __name__ in "__main__":
    da = Dankook(re_notice_type='cheonan',re_univ_name='test')
    da1 = Dankook(re_notice_type='common',re_univ_name='test')