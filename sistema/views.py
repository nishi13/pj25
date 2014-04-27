# imports
from django.db import models
from django import forms
# from sistema.forms import *
from sistema.models import *
from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext

from sistema.forms import *
from sistema.models import *

# functions
def home (request):
	return HttpResponseRedirect('/egplus')

def evento (request, evento_sigla):
    evento = Evento.objects.get(sigla = evento_sigla)
    confirmados = Membro.objects.filter(evento=evento)
    anos = {}
    for pessoa in confirmados:
		if (anos[pessoa.ano_de_saida]):
			anos[pessoa.ano_de_saida].append (pessoa)
 		else:
            obj[asd.ano]=[asd]
    if request.method == 'GET':
        membro_form = MembroForm()
    else:
        membro_form = MembroForm(request.POST)
        if membro_form.is_valid():
            membro = membro_form.save(commit = False)
            membro.evento = evento
            membro.save()
            membro_form = MembroForm()
    try:
        return render_to_response (evento_sigla+'.html', locals(), context_instance = RequestContext(request))
    except :
        return render_to_response ('base.html', locals(), context_instance = RequestContext(request))
