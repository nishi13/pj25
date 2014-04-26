# imports
from django.db import models
from django import forms
# from sistema.forms import *
from sistema.models import *
from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext

# functions
def home (request):

	return HttpResponseRedirect('/egplus')

def egplus (request):

	return render_to_response ('egplus.html', locals(), context_instance = RequestContext(request))