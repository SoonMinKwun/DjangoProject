'''
이 파일은 최초 1회 종목들의 정보를 불러와서 DB에 넣기 위한 파일입니다. 1회만 실행하면 완료.
'''

import pandas as pd
import usingDf
import opinion_mining
import pymongo 
import traceback

# DB insert
def makeEmotion():
    comments =  usingDf.Crawling_comment.get_comment()
    comments_emotion = []   #pymongo 쓸때 형식이 List이어야 함
    for  key, val in comments.items():
        if key != None:
            comments_emotion.append({"stock" : key , "feeling"  : opinion_mining.Opinion_Mining.mining(str(val)) ,"comments" : val})
    if comments_emotion != None:
        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        mydb = myclient["Stock_Emo_DB"]
        mycol = mydb["Stock_Emo_App_stock"]
        x = mycol.insert_many(comments_emotion)
        return x

comments_emotion = makeEmotion()