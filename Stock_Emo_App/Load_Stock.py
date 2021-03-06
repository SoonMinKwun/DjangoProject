'''
이 파일은 DB에 있는 값을 메인페이지에 불러오기 위한 기능을 담은 파일입니다.
'''

import pymongo
 
class Load_Stock:
    _instance = None
    client = pymongo.MongoClient( host='localhost',
                                  port=27017)
    database = client['Stock_Emo_DB']['Stock_Emo_App_stock']
 
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = object.__new__(cls, *args, **kwargs)
        return cls._instance
 
    def get_stocks_from_collection(cls, _query):
        assert cls.database
        return cls.database.find( _query)