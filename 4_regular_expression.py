import re

url = "ca.e"
p = re.compile(url)

# . 하나의 문자   ex) ca.e / care
# ^ 문자열의 시작  ex) ^de / desk
# $ 문자열의 끝   ex) se$ / case


def print_match(m):
    if m:
        print(m.group()) # 일치하는 문자열만 반환
        print(m.string) # 입력받은 문자열 반환
        print(m.start()) # 일치하는 문자열의 시작 인덱스
        print(m.end()) # 일치하는 문자열의 끝 인덱스
        print(m.span()) # 일치하는 문자열의 시작과 끝 인덱스
    else:
        print("매칭 안됨")


m = p.match("caseless")
print_match(m)
# match는 주어진 문자열이 처음부터 일치하는지 확인
m = p.search("careless")
print_match(m)
# search는 주어진 문자열 중 일치하는게 있는지 확인
m_list = p.findall("good care cafe")
print(m_list)
# findall은 일치하는 모든 것을 리스트 형태로 반환

# 1. re.compile("원하는 형태")
# 2. m = p.match("비교할 문자열")
# 3. m = p.search("비교할 문자열")
# 4. 1st = p.findall("비교할 문자열")