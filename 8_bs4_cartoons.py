import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/list.nhn?titleId=748105"
res = requests.get(url)
res.raise_for_status()# 문제가 생기면 err 코드 내보내고 프로그램 종료

soup = BeautifulSoup(res.text, "lxml")

cartoons = soup.find_all("td", attrs={"class":"title"}) #td태그의 title class를 모두 카툰이라는 list에 저장

# title = cartoons[0].a.get_text() # 0번째 list의 a tag의 text
# link = cartoons[0].a["href"] # 0번쨰 list의 a 태그의 href 속성
#
# print(title)
# print("https://comic.naver.com" + link)

# 만화 제목 + 링크 가져오기
# for cartoon in cartoons:
#     title = cartoon.a.get_text()
#     link = cartoon.a["href"]
#     print(title)
#     print("https://comic.naver.com" + link)

# 평점 구하기
