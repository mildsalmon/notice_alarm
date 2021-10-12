> 관련 개발일지는 아래 링크를 참고해주세요.
> 
> [블로그 개발일지](https://blex.kr/@mildsalmon/series/%ED%95%9C%EB%9D%BC%EB%8C%80%ED%95%99%EA%B5%90-%EA%B3%B5%EC%A7%80-%EC%95%8C%EB%A6%BC-%EB%B4%87-%EC%A0%9C%EC%9E%91%EA%B8%B0)

# notice_alarm

한라대학교, 단국대학교(천안) 최신 공지사항을 읽어서 텔레그램 봇 채널로 전송하는 소스코드입니다.

# 1. 기획 배경

새로운 공지사항이 게시되었는지 확인하기 위해 매번 학교 홈페이지에 접속하는 것이 번거로웠다. "내가 불편한 것은 다른 사람들도 불편하겠지?"라는 생각이 들어서 재학생들도 자유롭게 이용할 수 있도록 새로운 공지사항을 알려주는 텔레그램 채널을 개설해서 운영하였다. 

# 2. 성과

### a. 기대효과

- 새로운 공지사항을 확인하기 위해 학교 홈페이지에 접속하는 시간이 절약됨.

# 3. 도식화

### A. 시스템 흐름도

![d-day 프로그램_시스템구성](/image/system_flow.png)

# 4. 서비스 캡쳐

![서비스중인 텔레그램 채널](/image/run.png)

# 5. 서비스 채널

[Dankook_notice_alarm_service](https://t.me/dankook_notice_alarm)

[Halla_notice_alarm](https://t.me/halla_notice_Alarm)

# 6. 개발 환경 설정

### A. 프로그래밍 언어

- Python (3.7)

##### a. 파이썬 주요 라이브러리

- beautifulsoup4 (4.9.3)
- python-telegram-bot
