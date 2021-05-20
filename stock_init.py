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

# DB연결
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["Stock_Emo_DB"]
mycol = mydb["Stock_Emo_App_stock"]

# DB 값과 최신 크롤링 값을 데이터프레임으로 비교
DB = list(mycol.find())
latest = latest_emotion()

df1 = pd.DataFrame(DB)
df2 = pd.DataFrame(latest)

# DB의 feeling과 최신 크롤링한 feeling이 같은 것만 데이터프레임으로 추출
latest_df = df2[df1['feeling'] != df2['feeling']]

# 추출된 데이터프레임을 딕셔너리로 변환
latest_dict = dict(zip(latest_df['stock'],latest_df['feeling']))
'''
latest_dict는 아래처럼 리턴
{'AAPL': 'joy', 'GOOG': 'joy', 'GOOGL': 'joy', 'TSLA': 'sadness', 'FB': 'joy', 'TSM': 'sadness', 'V': 'anger', 'JNJ': 'disgust', 'JPM': 'guilt', 'DIS': 'sadness', 'HD': 'sadness', 'PYPL': 'fear', 'BAC': 'joy'}
'''

# 추출된 latest_dict를 리스트 안에 담기
latest_list = [latest_dict]
print(latest_list)
print(type(latest_list))
print(df2)

# 추출된 latest_list(종목명, 감정, 코멘트)를 DB에 삽입
for i in latest_list:
    for stock, feeling in i.items():
        is_changed = df2['stock'] == stock  # 종목명이 같으면
        comments = df2[is_changed]['comments'].tolist()[0]  # 종목명이 같은 행의 comments 열만 추출해서 리스트 안에 담기(이중 리스트라서 [0] 붙힘)
        mycol.update_one({'stock' : stock} , {'$set' : {'feeling' : feeling , 'comments' : comments}})