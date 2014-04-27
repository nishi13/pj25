from django.db import models
import os

def upload_template (instance, filename):
    filename = "%s.html" % (instance)
    return os.path.join('sistema/templates', filename)

def upload_css (instance, filename):
    filename = "%s.css" % (instance)
    return os.path.join('static/css', filename)

def upload_logo (instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (instance, ext)
    return os.path.join('static/logo', filename)

def upload_imagem (instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (instance.id, ext)
    return os.path.join('static/logo', filename)

class Cargo(models.Model):
    nome = models.CharField(max_length=64, verbose_name="Cargo / Ultimo Cargo", primary_key=True)

    def __unicode__(self):
        return self.nome

class Evento(models.Model):
    sigla = models.CharField(max_length=8, verbose_name="Sigla", primary_key=True)
    nome = models.CharField(max_length=64, verbose_name="Nome")
    titulo = models.CharField(max_length=128, verbose_name="Titulo")
    rgb_primario = models.CharField(max_length=6, null=True, blank=True, verbose_name="RGB Primario")
    rgb_secundario = models.CharField(max_length=6, null=True, blank=True, verbose_name="RGB Secundario")
    template = models.FileField(upload_to=upload_template, null=True, blank=True)
    css = models.FileField(upload_to=upload_css, null=True, blank=True)
    logo = models.FileField(upload_to=upload_logo, null=True, blank=True)

    def __unicode__(self):
        return self.nome

class Membro(models.Model):
    nome = models.CharField(max_length=128, verbose_name="Nome Completo")
    apelido = models.CharField(max_length=64, null=True, blank=True, verbose_name="Apelido")
    ano_de_ingresso = models.IntegerField(null=True, blank=True, verbose_name="Ano de Ingresso")
    ano_de_saida = models.IntegerField(null=True, blank=True, verbose_name="Ano de Saida")
    email = models.EmailField(max_length=128, verbose_name="E-mail")
    cargo = models.ForeignKey(Cargo)
    evento = models.ForeignKey(Evento)
    
    def __unicode__(self):
        return self.nome

class Imagem(models.Model):
    titulo = models.CharField(max_length=128, verbose_name="Titulo", null=True, blank=True)
    subtitulo = models.CharField(max_length=128, verbose_name="Titulo", null=True, blank=True)
    arquivo = models.FileField(upload_to=upload_imagem)
