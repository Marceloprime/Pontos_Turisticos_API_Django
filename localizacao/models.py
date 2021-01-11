# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Localizacao(models.Model):
    nome = models.CharField(max_length=150)
    rua = models.CharField(max_length=150)
    bairro = models.CharField(max_length=150)
    cidade = models.CharField(max_length=150)
    estado = models.CharField(max_length=150)
    pais = models.CharField(max_length=150)
    ponto_de_referencia = models.CharField(max_length=150)
    latitude = models.IntegerField(null=True,blank=True)#campo de prenchimento opcional
    longitude = models.IntegerField(null=True,blank=True)#campo de prenchimento opcional

    def __str__(self):
        return self.nome



