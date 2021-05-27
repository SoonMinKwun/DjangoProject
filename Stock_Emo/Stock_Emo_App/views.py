from django.shortcuts import render
from .models import Stock


def index(request):
    return render(request, 'Stock_Emo_App/main.html')