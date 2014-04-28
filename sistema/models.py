from django.db import models
import os

def replace (path):
    if os.path.exists(path):
        os.remove(path)
    return path

def upload_template (instance, filename):
    pathname = "%s.html" % (instance)
    file_save = os.path.join('sistema/templates', pathname)
    return replace (file_save)

def upload_css (instance, filename):
    pathname = "%s.css" % (instance)
    file_save = os.path.join('static/css', pathname)
    return replace (file_save)

def upload_logo (instance, filename):
    ext = filename.split('.')[-1]
    pathname = "%s.%s" % (instance, ext)
    file_save = os.path.join('static/images/logo', pathname)
    return replace (file_save)

def upload_imagem (instance, filename):
    pathname = "%s_%s" % (instance.evento.sigla, filename)
    return os.path.join('static/images/fotos', pathname)

def upload_perfil (instance, filename):
    ext = filename.split('.')[-1]
    pathname = "%s.%s" % (instance.id, ext)
    file_save = os.path.join('static/images/perfil', pathname)
    return replace (file_save)

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
    logo = models.FileField(upload_to=upload_logo, null=True, blank=True)
    local = models.CharField(max_length=256, verbose_name="Local", null=True, blank=True)
    template = models.FileField(upload_to=upload_template, null=True, blank=True)
    css = models.FileField(upload_to=upload_css, null=True, blank=True)
    data = models.CharField(max_length=64, verbose_name="Data")
    traje = models.CharField(max_length=64, verbose_name="Traje", null=True, blank=True)
    descricao = models.TextField(max_length=1024, verbose_name="Mensagem", null=True, blank=True)

    def __unicode__(self):
        return self.sigla

class Membro(models.Model):
    nome = models.CharField(max_length=128, verbose_name="Nome Completo *")
    apelido = models.CharField(max_length=64, null=True, blank=True, verbose_name="Apelido")
    ano_de_ingresso = models.IntegerField(verbose_name="Ano de Ingresso *")
    ano_de_saida = models.IntegerField(verbose_name="Ano de Saida", null=True, blank=True)
    email = models.EmailField(max_length=128, verbose_name="E-mail *", unique=True)
    cargo = models.ForeignKey(Cargo, verbose_name="Cargo *")
    facebook = models.URLField(max_length=256, null=True, blank=True)
    twitter = models.URLField(max_length=256, null=True, blank=True)
    linkedin = models.URLField(max_length=256, null=True, blank=True)
    foto = models.FileField(upload_to=upload_perfil, null=True, blank=True, verbose_name="Foto de Perfil")
    confirmado = models.BooleanField(verbose_name="Estarei Presente", default=True)
    mensagem = models.TextField(max_length=1024, verbose_name="Mensagem", null=True, blank=True)
    horario_do_submit = models.DateTimeField(auto_now = True)
    evento = models.ForeignKey(Evento)
    
    def __unicode__(self):
        return self.nome

class Imagem(models.Model):
    evento = models.ForeignKey(Evento);
    titulo = models.CharField(max_length=128, verbose_name="Titulo", null=True, blank=True)
    subtitulo = models.CharField(max_length=128, verbose_name="Titulo", null=True, blank=True)
    arquivo = models.FileField(upload_to=upload_imagem)
