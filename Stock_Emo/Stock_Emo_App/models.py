from django.db import models

class Stock(models.Model):
    stock_ticker = models.CharField(max_length=30)
    stock_price = models.IntegerField(default=0)
    stock_talk = models.CharField(max_length=1000000)
    stock_date = models.DateTimeField('date published')
    stock_emo = models.CharField(max_length=15)
    
class Member(models.Model):
    mem_email = models.CharField(max_length=30)
    mem_pw = models.CharField(max_length=15)
    mem_name = models.CharField(max_length=10)