from module.notice_alarm import NoticeAlarm
import requests
from bs4 import BeautifulSoup
import os


class Halla(NoticeAlarm):
    def __init__(self, re_notice_type, re_univ_name='halla'):
        BASE_DIR = os.path.join(os.path.dirname(os.path.abspath(os.path.dirname(__file__))), "data_file")

        self.notice_type = {'일반': 'normal',
                            '학사': 'academic'}

        if re_notice_type == self.notice_type['일반'] or re_notice_type == self.notice_type['학사']:
            url = "http://www.halla.ac.kr/mbs/kr/jsp/board/"

        super().__init__(re_univ_name=re_univ_name, re_notice_type=re_notice_type)

        if re_notice_type == self.notice_type['일반']:
            self.req = requests.get(url + "list.jsp?boardId=23401&mcategoryId=&id=kr_060101000000")
        elif re_notice_type == self.notice_type['학사']:
            self.req = requests.get(url + "list.jsp?boardId=23409&id=kr_060102000000")

        if not(self.web_errors(status_code_req=self.req.status_code)):
            self.exit()

        save_boardSeq, posts, use_boardSeq = self.html_analyze()

        if not (os.path.isfile(os.path.join(BASE_DIR, self.file_name))):
            self.write_file(save_content=save_boardSeq)

        old_data = self.open_file()
        self.matching(posts=posts, use_boardSeq=use_boardSeq, chat_id=self.show_chat_id(), re_url=url)
        self.write_file(save_content=save_boardSeq)

    # 한라대 클래스로 분리
    # 한라대 html 분석
    def html_analyze(self):
        html = self.req.text
        soup = BeautifulSoup(html, 'html.parser')
        # 한라대의 경우 일반공지와 학사공지 크롤링 방식이 같다.
        if self.notice_type['일반'] or self.notice_type['학사']:
            posts = soup.select('td > a')
        notice_num = len(soup.find_all(title='공지'))  # 새로운 게시글이 아닌 공지 글 개수를 카운트
        save_boardSeq = []
        use_boardSeq = []

        for i in range(notice_num):  # 게시글을 제외한 공지 글 제거
            del posts[0]

        for post in posts:
            save_boardSeq.append(str(post).split("&amp")[2])  # local에 파일로 저장할 내용
            use_boardSeq.append(str(post).split("&amp;")[2])  # 이 코드에서 실행할 내용

        save_boardSeq[0] = save_boardSeq[0].lstrip(";")
        #
        return save_boardSeq, posts, use_boardSeq


if __name__ in "__main__":
    ha = Halla("normal", 'test')

