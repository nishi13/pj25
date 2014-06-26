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
    cargos = Cargo.objects.all().order_by('nome')
    imagens = Imagem.objects.filter(evento=evento)
    confirmados = Membro.objects.filter(evento=evento).filter(confirmado=True).order_by('nome')
    mensagens = Membro.objects.filter(evento=evento).filter(mensagem__isnull=False).exclude(mensagem="").order_by('-horario_do_submit')
    anos = {}
    for pessoa in confirmados:
        try:
            anos[pessoa.ano_de_saida].append(pessoa)
    	except:
            anos[pessoa.ano_de_saida]=[pessoa]
    lista=[]
    for key,value in anos.iteritems():
        if key:
            lista.append((key,value))
        else:
            lista.append(('Membros Atuais',value))
    lista=sorted(lista)
    if request.method == 'GET':
        membro_form = MembroForm()
    else:
        membro_form = MembroForm(request.POST, request.FILES)
        cargo = request.POST.get("cargo")
        if cargo == '--Adicionar--':
            cargo = request.POST.get("cargo_add").capitalize()
            membro_form.data['cargo']=cargo
            if cargo:
                Cargo.objects.get_or_create(nome=cargo)
        if membro_form.is_valid():
            membro = membro_form.save(commit = False)
            membro.evento = evento
            membro.save()
            membro_form = MembroForm()
            return HttpResponseRedirect('#services')
    try:
        return render_to_response (evento_sigla+'.html', locals(), context_instance = RequestContext(request))
    except :
        return render_to_response ('base.html', locals(), context_instance = RequestContext(request))
