import notice_alarm
import requests
from bs4 import BeautifulSoup
import name_list

name_list_notice_type = name_list.name_list_notice_type()
name_list_univ_name = name_list.name_list_univ_name()

class halla(notice_alarm.NoticeAlarm):
    def __init__(self, univ_name, notice_type):
        url = "http://www.halla.ac.kr/mbs/kr/jsp/board/"

        super().__init__(univ_name, notice_type, url)

        self.univ_name = univ_name
        self.req = ""
        if notice_type == name_list_notice_type[0]:
            self.req = requests.get("http://www.halla.ac.kr/mbs/kr/jsp/board/list.jsp?boardId=23401&mcategoryId=&id=kr_060101000000")
        elif notice_type == name_list_notice_type[1]:
            self.req = requests.get("http://www.halla.ac.kr/mbs/kr/jsp/board/list.jsp?boardId=23409&id=kr_060102000000")
        print(self.web_errors(self.req.status_code))
        self.html_analyze()


    # 한라대 클래스로 분리
    # 한라대 html 분석
    def html_analyze(self):
        html = self.req.text
        soup = BeautifulSoup(html, 'html.parser')
        if self.univ_name == name_list_univ_name[0]:   # 한라대의 경우 일반공지와 학사공지 크롤링 방식이 같다.
            self.posts = soup.select('td > a')
            notice_num = len(soup.find_all(title='공지')) # 새로운 게시글이 아닌 공지 글 개수를 카운트
            self.save_boardSeq = []
            self.use_boardSeq = []

            for i in range(notice_num): # 게시글을 제외한 공지 글 제거
                del self.posts[0]

            for post in self.posts:
                self.save_boardSeq.append(str(post).split("&amp")[2])    # local에 파일로 저장할 내용
                self.use_boardSeq.append(str(post).split("&amp;")[2])    # 이 코드에서 실행할 내용

            self.save_boardSeq[0] = self.save_boardSeq[0].lstrip(";")
        #
        # return save_boardSeq, posts, use_boardSeq

if __name__ in "__main__":
    ha = halla("한라", "일반")
    print(type(ha.req))