# 목표
# 1. 페이지를 입력하면 그 사이트를 크롤링
# 2. 키워드를 입력하면 해당 키워드를 검색
# 3. 몇 초에 한 번씩 반복하는지 입력
# 4. 키워드가 검색되면 루프를 멈추고 어떠한 형태로 알람을 보냄

import requests
from bs4 import BeautifulSoup

continue_check = 1

while continue_check == 1:
    print("# This is Keyword Crawler.")
    url = input("# Please enter the page url: ")
    keyword = input("# Please enter the keyword: ")
    term = input("# Please enter the term of searching: ")

    try:
        response = requests.get(url)
    except requests.exceptions.InvalidSchema:
        print("# !!! Wrong url\n")
        continue
    except requests.exceptions.MissingSchema:
        print("# !!! Wrong url\n")
        continue

    html = ""

    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
    else:
        print("# !!! Crawling page failed: " + response.status_code + "\n")

    items = soup.select("span.ellipsis-with-reply-cnt")
    for item in items:
        print(item)
        x = item.find(keyword)
        print(item)