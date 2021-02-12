import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday.nhn"
res = requests.get(url)
res.raise_for_status() # 문제가 생기면 err 코드 내보내고 프로그램 종료

soup = BeautifulSoup(res.text, "lxml") #lxml paser를 통해서 beautifulsoup 객체로 만듬 -> soup이 파싱된 자료를 나타내게됨

# print(soup.title)
# print(soup.title.get_text())
#
# print(soup.a) # soup객체 중 1번쨰로 발견된 a element 정보를 출력함
# print(soup.a.attrs) # attribute 속성 부여(dictionary 형태로 출력)
# print(soup.a["href"]) # soup객체 / 1번쨰 a에서 href 속성값 출력

# print(soup.find("a", attrs={"class":"Nbtn_upload"}))

# print(soup.find("li", attrs={"class":"rank01"}))
#
##### rank1 = soup.find("li", attrs={"class":"rank01"})
# print(rank1.a) # rank1 객체 중 1번째로 발견된 a element 정보 출력, soup로 find 한 객체에서 하위객체 불러오기 가능
# print(rank1.a.get_text())
# rank2 = rank1.next_sibling.next_sibling # 다음 형제 element 출력 해당 next_sibling*2는 줄바꿈으로 인한 예외처리 -> rank1.find_next_sibling() # 조건부 next sibling 찾기

# print(rank1.find_next_sibling("li")) # rank2 = rank1.find_next_sibling("li")

# rank3 = rank2.next_sibling.next_sibling
# rank2 = rank3.previous_sibling.previous_sibling # 이전 형제 element 출력법
# print(rank3.a.get_text())

# print(rank1.parent) # rank1의 부모 및 하위 자식 element까지 전부 출력

webtoon = soup.find("a", text="개를 낳았다-시즌2 38화") # text는 tag 사이의 글자를 뜻함
# ex) <a onclick="nclk_v2(event,'rnk*p.cont','712362','4')" href="/webtoon/detail.nhn?titleId=712362&amp;no=109" title="개를 낳았다-시즌2 38화">개를 낳았다-시즌2 38화</a>
# text = 외모지상주의-325화 클럽
print(webtoon)