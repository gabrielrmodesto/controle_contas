from django.shortcuts import render
from .models import Transacao
import datetime

def home(request):
    data = {}

    return render(request, 'contas/home.html', data)

def listagem(request):
    data = {}
    data['transacoes'] = Transacao.objects.all()
    return render(request, 'contas/listagem.html', data)