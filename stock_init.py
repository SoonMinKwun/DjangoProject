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

# DB update
def confirm_emotion(comments_emotion):
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["Stock_Emo_DB"]
    mycol = mydb["Stock_Emo_App_stock"]
    inDB = list(mycol.find())
    print(inDB)
    #만약에 크롤링한 값과 db의 있는 값중에  stcok이 같고
    # 1)감정이 다를 경우 -> 업데이트 한다
    # 2)감정이 같은 경우 -> 무시한다



# 크롤링한 댓글들을 하나의 문자열로 합치기
#all_comments = (' '.join(comments))
comments_emotion = makeEmotion()
