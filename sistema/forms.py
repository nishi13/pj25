from django.forms import ModelForm
from django import forms
from sistema.models import *


class MembroForm (forms.ModelForm):
    class Meta :
        model = Membro

class EventoForm (forms.ModelForm):
    class Meta :
        model = Evento

class CargoForm (forms.ModelForm):
    class Meta :
        model = Cargo