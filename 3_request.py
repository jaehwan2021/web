import requests
res = requests.get("http://google.com")
res.raise_for_status() # 200 code 아닐시 code err 발생
with open("googlefile.html", "w", encoding="utf8") as f:
    f.write(res.text)


