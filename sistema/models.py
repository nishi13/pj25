from django.db import models

# Create your models here.

class Cargo(models.Model):
    nome = models.CharField(max_length=64, null=True, blank=True, verbose_name="Cargo / Ultimo Cargo")

    def __unicode__(self):
        return self.nome
        
class Membros(models.Model):
    
    nome = models.CharField(max_length=128, verbose_name="Nome Completo")
    apelido = models.CharField(max_length=64, null=True, blank=True, verbose_name="Apelido")
    ano_de_ingresso = models.IntegerField(null=True, blank=True, verbose_name="Ano de Ingresso")
    ano_de_saida = models.IntegerField(null=True, blank=True, verbose_name="Ano de Saida")
    email = models.EmailField(max_length=128, verbose_name="E-mail")
    cargo = models.ForeignKey(Cargo)
    
    def __unicode__(self):
        return self.nome
