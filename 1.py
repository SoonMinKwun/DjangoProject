import usingDf
import pandas as pd

#print(usingDf.Crawling_comment.get_comment()[0])
#print(len(usingDf.Crawling_comment.get_comment()))

comments = usingDf.Crawling_comment.get_comment()

#첫번째 코멘트
print(comments[0])

#코멘트 갯수
last = len(comments)
print("Number of comments: " + str(last-1))

#종목명
stock_code = comments[last-1]
print(stock_code)

#코멘트
for i in range(last-2):
    print(comments[i])