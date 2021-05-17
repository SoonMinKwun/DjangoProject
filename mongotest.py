'''
MongoDB TEST
'''

import pymongo



myclient = pymongo.MongoClient("mongodb://localhost:27017/")



mydb = myclient["Stock_Emo_DB"]

mycol = mydb["Stock_Emo_App_stock"]



mydict = { "name": "John", "address": "Highway 37" }

x = mycol.insert_one(mydict)