from django.shortcuts import render
from .models import Stock
from django.http import HttpResponse
from django.template import loader
from Stock_Emo_App.Load_Stock import Load_Stock


# def index(request):
#     return render(request, 'Stock_Emo_App/main.html')
 
def specific_stock(request, stock):
    def get():
        dbStockData = Load_Stock().get_stocks_from_collection({'stock': stock})

        stockData = dbStockData[0]
        del stockData['_id']
 
        template = loader.get_template('Stock_Emo_App/main.html')
        return HttpResponse(template.render({'stockData':[stockData]}, request))
 
    if request.method == 'GET':
        return get()
    else:
        return HttpResponse(status=405)
 
def all_stocks(request):
    def get():
        dbStockData = Load_Stock().get_stocks_from_collection({})

        stockData = []
        for stock in dbStockData:
            del stock['_id']
            stockData.append(stock)

        template = loader.get_template('Stock_Emo_App/main.html')
        return HttpResponse(template.render({'stockData': stockData}, request))
 
    if request.method == 'GET':
        return get()
    else:
        return HttpResponse(status=405)