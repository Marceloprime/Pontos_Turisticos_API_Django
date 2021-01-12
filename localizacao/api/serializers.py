from localizacao.models import Localizacao
from rest_framework.serializers import ModelSerializer


class LocalizacaoSerializer(ModelSerializer):
    class Meta:
        model = Localizacao
        fields = ['nome', 'rua', 'bairro', 'cidade', 'estado', 'pais', 'ponto_de_referencia', 'latitude', 'longitude']