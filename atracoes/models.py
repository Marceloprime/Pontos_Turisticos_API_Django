# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Atracao(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    horario = models.TextField()
    idade_min = models.IntegerField()

    def __str__(self):
        return self.nome