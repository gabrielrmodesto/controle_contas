from django.forms import ModelForm
from .models import Transacao

class TransacaForm(ModelForm):
    class Meta:
        model = Transacao
        fields = ['data', 'descricao', 'valor', 'observacao', 'categoria']