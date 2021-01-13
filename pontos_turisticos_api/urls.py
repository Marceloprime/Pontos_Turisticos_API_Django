"""pontos_turisticos_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from rest_framework import routers

from pontos_turisticos.api.viewsets import PontoTuristicoViewSet
from atracoes.api.viewsets import AtracaoViewSet
from avaliacoes.api.viewsets import AvaliacaoViewSet
from comment.api.viewsets import ComentarioViewSet
from localizacao.api.viewsets import LocalizacaoViewSet


router = routers.DefaultRouter()
router.register(r'ponto',PontoTuristicoViewSet, basename='PontoTuristico')
router.register(r'atracoes',AtracaoViewSet)
router.register(r'avaliacoes',AvaliacaoViewSet)
router.register(r'comment',ComentarioViewSet)
router.register(r'localization',LocalizacaoViewSet)


urlpatterns = [
    path('',include(router.urls)),
    url(r'^admin/', admin.site.urls),
]
