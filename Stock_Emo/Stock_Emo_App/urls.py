from django.urls import path

from . import views

app_name = 'Stock_Emo_App'

urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.all_stocks, name='index'),
    path('<stock>', views.specific_stock, name='HtmlSpecificStock'),
]