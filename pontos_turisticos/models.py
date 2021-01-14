# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from atracoes.models import Atracao
from comment.models import Comentario
from avaliacoes.models import Avaliacao
from localizacao.models import Localizacao
from django.db import models

# Create your models here.
class PontoTuristico(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    aprovado = models.BooleanField(default=False)
    atracoes = models.ManyToManyField(Atracao)
    comments = models.ManyToManyField(Comentario)
    avaliacoes = models.ManyToManyField(Avaliacao)
    localizacao = models.ForeignKey(
        Localizacao,on_delete=models.CASCADE,null=True,blank=True)
    foto = models.ImageField(upload_to = 'pontosImages', null=True, blank=True)

    def __str__(self):
        return self.nome