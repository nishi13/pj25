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

def evento (request, evento_nome):
    membro_form = MembroForm()
    try:
        return render_to_response (evento_nome+'.html', locals(), context_instance = RequestContext(request))
    except :
        return render_to_response ('base.html', locals(), context_instance = RequestContext(request))