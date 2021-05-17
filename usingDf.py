'''
이 파일은 엑셀로 시가총액순 종목을 추출하여 크롤링한 내용을 딕셔너리로 추출하는 파일입니다.
'''

from numpy.lib.type_check import common_type
import pandas as pd
import crawling_title

stock_xlsx = pd.read_excel("./20210124.xlsx")
stock_xlsx = stock_xlsx.dropna()
stock_xlsx.sort_values(by = '시가총액' , ascending= False  ,inplace = True )
#print(stock_xlsx[['종목코드','시가총액']][:100])



# 크롤링 추출하는 Class
class Crawling_comment:
    def get_comment():
        comment = dict()    # 종목명이랑 크롤링한 내용을 딕셔너리로 분류
        for stock_code in stock_xlsx['종목코드'][:20]:
            comment[stock_code] = crawling_title.Crawling_title(stock_code).get_comment()   
        return comment