import requests
url = "http://nadocoding.tistory.com"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.146 Safari/537.36"}
res = requests.get(url, headers=headers) # 유저에이전트 값을 넣어준 상태로 url 접속 진행
res.raise_for_status() # 200 code 아닐시 code err 발생
with open("nadocoding.html", "w", encoding="utf8") as f:
    f.write(res.text)