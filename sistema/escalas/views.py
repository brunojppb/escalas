import json
from django.shortcuts import render

#from django.template.loader import get_template
from django.http import HttpResponseRedirect, HttpResponse
from sistema.escalas.models import Militar, Guarnicao
from sistema.escalas.forms import *

def home(request):
    return render(request, 'home.html', {})



def guarnicao_detalhes(request, ident):
	guarnicao = Guarnicao.objects.get(id=ident)
	militares = guarnicao.militar_set.all()
	return render(request, 'guarnicao/guarnicao_detalhes.html', {'guarnicao': guarnicao, 'militares': militares})

def guarnicao_listar(request):
	guarnicoes = Guarnicao.objects.all()
	return render(request, 'guarnicao/guarnicao_lista.html', {'guarnicoes': guarnicoes})

def guarnicao_criar(request):
    error = False
    if request.method == 'POST':
        nome = request.POST.get('nome', '')
        missao = request.POST.get('missao', '')
        militares = request.POST.getlist('militares[]')
        if nome != '' and missao != '':
            guarnicao = Guarnicao()
            guarnicao.nome = nome
            guarnicao.missao = missao
            guarnicao.save()
            for ident in militares:
                militar = Militar.objects.get(id=ident)
                militar.guarnicao = guarnicao
                militar.save()
            return HttpResponseRedirect('/escalas/guarnicao/listar/')
        else:
            error = True
            return render(request, 'guarnicao/guarnicao_form.html', {'error': error})
    else:
        return render(request, 'guarnicao/guarnicao_form.html')

def militar_detalhes(request, mat):
    militar = Militar.objects.get(matricula=mat)
    return render(request, 'militar/militar_detalhes.html', {'militar': militar})

def militar_listar(request):
    militares = Militar.objects.all()
    return render(request, 'militar/militar_lista.html', {'militares': militares})

def militar_criar(request):
    error = False
    form = MilitarForm()
    if request.method == 'POST':
        militar = MilitarForm(request.POST)
        if militar.is_valid():
            militar.save()
            return HttpResponseRedirect('/escalas/militar/listar')
        else:
            error = True
            return render(request, 'militar/militar_form.html', {'error': error})
    else:
        return render(request, 'militar/militar_form.html', {'form': form})

def militar_editar(request, ident):
    if request.method == 'POST':
        militar = Militar.objects.get(id=int(ident))
        form = MilitarForm(request.POST, instance=militar)
        form.save()
        return HttpResponseRedirect('/escalas/militar/listar')
    else:
        militar = Militar.objects.get(id=int(ident))
        form = MilitarForm(instance=militar)
        return render(request, 'militar/militar_form.html', {'form': form})


def ajax(request):
        nome = request.GET.get('q')
        militares = Militar.objects.filter(nome_de_guerra__icontains=nome)
        resultado = [{'id': m.id,
                    'nome': m.nome,
                    'posto': m.get_posto_display(),
                    'nome_de_guerra': m.nome_de_guerra,
                    'matricula': m.matricula,
                    'funcao': m.funcao
                    } for m in militares]
        return HttpResponse(json.dumps(resultado, sort_keys=True, indent=4), content_type="application/json")


def escala_criar(request):
    if request.method == 'POST':
        escala = EscalaForm(request.POST)
        if escala.is_valid():
            escala.save()
            return HttpResponseRedirect('/escalas/militar/listar/')

    else:
        escala = EscalaForm()
        return render(request, 'escala/escala_form.html', {'escala': escala})













