# -*- coding: utf-8 -*-

from django.core.management.base import NoArgsCommand
from sistema.models import *
from django.contrib.auth.models import User

membros = [
    {
        'nome' : 'Augusto Nishi',
        'apelido' : 'Nishi',
        'ano_de_ingresso' : '2011', 
        'ano_de_saida' : '2014',
        'email' : 'augusto.nishi@gmail.com',
    },{
        'nome' : 'Pedro Martinez',
        'apelido' : 'Pedrao',
        'ano_de_ingresso' : '2012', 
        'ano_de_saida' : '2015',
        'email' : 'pvsmartinez@gmail.com',
    },{
        'nome' : 'Milena Ming Perez',
        'apelido' : 'Ming',
        'ano_de_ingresso' : '2010', 
        'ano_de_saida' : '2013',
        'email' : 'mmpmilena@gmail.com',
    },{
        'nome' : 'Joao Ninguem',
        'apelido' : 'Joao',
        'ano_de_ingresso' : '2008', 
        'ano_de_saida' : '2008',
        'email' : 'joao@ninguem.com',
    }
]

class Command(NoArgsCommand):
    help = '''Cria Grupos'''
    requires_model_validation = 0
        
    def handle_noargs(self, **options):
        
        user = User.objects.create_user('admin', 'admin@admin.com', 'admin')
        user.is_superuser = True
        user.is_staff = True
        user.save()

        egplus = Evento('egplus','EG Plus', 'Conectando Gerações','004E95','FBAA26')
        egplus.save()

        analista = Cargo('Analista')
        analista.save()

        gerente = Cargo('Gerente')
        gerente.save()

        diretor = Cargo('Diretor')
        diretor.save()

        conselho = Cargo('Conselho')
        conselho.save()

        cargos = [analista,gerente,diretor,conselho]

        for membro in membros:
            memb = Membro(**membro)
            memb.cargo = cargos.pop()
            memb.evento = egplus
            memb.confirmado = True
            memb.save()
