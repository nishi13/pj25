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
def evento (request, evento_sigla):
    evento = Evento.objects.get(sigla = evento_sigla)
    imagens = Imagem.objects.filter(evento=evento)
    confirmados = Membro.objects.filter(evento=evento).filter(confirmado=True).order_by('nome')
    anos = []
    for pessoa in confirmados:
    	flag = 1
    	for ano in anos:
    		if ano == pessoa.ano_de_saida:
    			flag = 0
    			break
    	if flag:
    		anos.append(pessoa.ano_de_saida)
    		anos.sort()
    if request.method == 'GET':
        membro_form = MembroForm()
    else:
        membro_form = MembroForm(request.POST, request.FILES)
        if membro_form.is_valid():
            membro = membro_form.save(commit = False)
            membro.evento = evento
            membro.save()
            membro_form = MembroForm()
            return HttpResponseRedirect('/'+evento_sigla+'/#services')
    try:
        return render_to_response (evento_sigla+'.html', locals(), context_instance = RequestContext(request))
    except :
        return render_to_response ('base.html', locals(), context_instance = RequestContext(request))
