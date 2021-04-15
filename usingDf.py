import pandas as pd
import crawling_title
stock_xlsx = pd.read_excel("./20210124.xlsx")
stock_xlsx = stock_xlsx.dropna()
stock_xlsx.sort_values(by = '시가총액' , ascending= False  ,inplace = True )
#print(stock_xlsx[['종목코드','시가총액']][:100])
for stock_code in stock_xlsx['종목코드'][:2]:
    print(crawling_title.Crawling_title(stock_code).get_comment())
