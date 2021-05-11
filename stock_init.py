import pandas as pd
import usingDf
import opinion_mining

# 시총순 회사들 크롤링한 댓글들
comments = usingDf.Crawling_comment.get_comment()

# 크롤링한 댓글들을 하나의 문자열로 합치기
all_comments = (' '.join(comments))

print(comments)