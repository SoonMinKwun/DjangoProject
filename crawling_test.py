import usingDf
import pandas as pd

#print(usingDf.Crawling_comment.get_comment()[0])
#print(len(usingDf.Crawling_comment.get_comment()))

comments = usingDf.Crawling_comment.get_comment()

# 크롤링한 댓글들을 하나의 문자열로 합치기
all_comments = (' '.join(comments))
print(all_comments)
print("-"*30)

#첫번째 코멘트
print("A first comment: " + comments[0])
print("-"*30)

#코멘트 갯수
last = len(comments)
print("Number of comments: " + str(last-1))
print("-"*30)

#종목명
stock_code = comments[last-1]
print("Stock Ticker: " + stock_code)
print("-"*30)

#코멘트
for i in range(last-2):
    print(comments[i])
print("-"*30)