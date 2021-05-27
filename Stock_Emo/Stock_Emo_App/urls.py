from django.urls import path

from . import views

app_name = 'Stock_Emo_App'

urlpatterns = [
    path('', views.index, name='index'),
]