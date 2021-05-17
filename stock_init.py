'''
이 파일은 크론탭을 이용하여 종목들의 상태를 업데이트 하는데에 필요한 파일입니다.
'''

#만약에 크롤링한 값과 db의 있는 값중에  stcok이 같고
# 1)감정이 다를 경우 -> 업데이트 한다
# 2)감정이 같은 경우 -> 무시한다

import pandas as pd
import usingDf
import opinion_mining
import pymongo 
import traceback

# 최신 크롤링 값
def latest_emotion():
    comments =  usingDf.Crawling_comment.get_comment()
    comments_emotion = []   #pymongo 쓸때 형식이 List이어야 함
    for  key, val in comments.items():
        if key != None:
            comments_emotion.append({"stock" : key , "feeling"  : opinion_mining.Opinion_Mining.mining(str(val)) ,"comments" : val})
    return comments_emotion

# DB 값 호출
def confirm_emotion():
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["Stock_Emo_DB"]
    mycol = mydb["Stock_Emo_App_stock"]
    inDB = list(mycol.find())
    return inDB

# DB 값과 최신 크롤링 값 비교
