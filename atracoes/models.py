# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Atracao(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    horario = models.TextField()
    idade_min = models.IntegerField()
    foto = models.ImageField(upload_to = 'atracoes', null=True, blank=True)

    def __str__(self):
        return self.nome