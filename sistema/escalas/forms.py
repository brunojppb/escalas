from django.forms import ModelForm, TextInput
from sistema.escalas.models import Militar, Escala, Guarnicao

class MilitarForm(ModelForm):
    class Meta:
        model = Militar
        widgets = {
            'nome': TextInput(attrs={'class': 'form-control'}),
            'nome_de_guerra': TextInput(attrs={'class': 'form-control'}),
            'matricula': TextInput(attrs={'class': 'form-control'}),
            'endereco': TextInput(attrs={'class': 'form-control'}),
            'data_de_nascimento': TextInput(attrs={'class': 'form-control'}),
            'calcado': TextInput(attrs={'class': 'form-control'}),
            'fardamento': TextInput(attrs={'class': 'form-control'}),
            'boina': TextInput(attrs={'class': 'form-control'}),
            'funcao': TextInput(attrs={'class': 'form-control'}),
        }

class EscalaForm(ModelForm):
    class Meta:
        model = Escala

class GuarnicaoForm(ModelForm):
    class Meta:
        model = Guarnicao
        widgets = {
            'nome': TextInput(attrs={'class': 'form-control'}),
            'missao': TextInput(attrs={'class': 'form-control'}),
        }