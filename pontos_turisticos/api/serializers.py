from pontos_turisticos.models import PontoTuristico
from rest_framework.serializers import ModelSerializer


class PontoTuristicoSerializer(ModelSerializer):
    class Meta:
        model = PontoTuristico
        fields = ['nome', 'descricao', 'aprovado', 'atracoes', 'comments', 'avaliacoes', 'localizacao']