from django.shortcuts import render, redirect
from .form import TransacaForm
from .models import Transacao


def home(request):
    data = {}

    return render(request, 'contas/home.html', data)

def listagem(request):
    data = {}
    data['transacoes'] = Transacao.objects.all()
    return render(request, 'contas/listagem.html', data)

def nova_transacao(request):
    form = TransacaForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('lista_transacao')

    return render(request, 'contas/form.html', {'form': form})

def update(request, pk):
    data = {}
    transacao = Transacao.objects.get(pk=pk)
    form = TransacaForm(request.POST or None, instance=transacao)

    if form.is_valid():
        form.save()
        return redirect('atualizar')

    data['form'] = form
    return render(request, 'contas/form.html', data)