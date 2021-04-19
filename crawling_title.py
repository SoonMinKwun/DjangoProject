from bs4 import BeautifulSoup
import requests
import re

#필요한거 stock code
class Crawling_title:
    def __init__(self ,stock_code):
        self.stock_code = stock_code
    def get_comment(self):
        result = [] #댓글 리스트
        plain ="https://finance.yahoo.com/quote/"+ self.stock_code + "/community?p" + self.stock_code
        html = requests.get(plain).text
        soup = BeautifulSoup(html, 'html.parser')
        posts = soup.find_all('div', {'class' : 'C($c-fuji-grey-l) Mb(2px) Fz(14px) Lh(20px) Pend(8px)'})
        #posts 의 type 는 beautifulsoup.resultSet  () -> text.strip()
        for i in posts:
            result.append(i.text.strip())
        return result