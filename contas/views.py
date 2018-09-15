from django.shortcuts import render
from django.http import HttpResponse
import datetime

def home(request):
    data = {}
    data['transacoes'] = ['t1','t3','t2']

    data['now'] = datetime.datetime.now()
    return render(request, 'contas/home.html', data)