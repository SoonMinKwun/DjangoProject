'''
이 파일은 크롤링을 실행하는 파일입니다. 종목별 코멘트 1페이지(20개의 코멘트)와 종목명(1개)을 포함하여
총 21개의 값을 가지고 있는 리스트를 추출하는 파일입니다.
'''

from bs4 import BeautifulSoup
import requests
import re

# 필요한거 stock code
class Crawling_title:
    def __init__(self ,stock_code):
        self.stock_code = stock_code
    def get_comment(self):
        result = [] # 댓글 리스트
        plain ="https://finance.yahoo.com/quote/"+ self.stock_code + "/community?p" + self.stock_code
        html = requests.get(plain).text
        soup = BeautifulSoup(html, 'html.parser')
        posts = soup.find_all('div', {'class' : 'C($c-fuji-grey-l) Mb(2px) Fz(14px) Lh(20px) Pend(8px)'})
        # posts 의 type 는 beautifulsoup.resultSet  () -> text.strip()
        for i in posts:
            result.append(i.text.strip())
        return result