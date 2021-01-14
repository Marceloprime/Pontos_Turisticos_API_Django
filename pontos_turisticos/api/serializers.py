from pontos_turisticos.models import PontoTuristico
from rest_framework.serializers import ModelSerializer
from atracoes.api.serializers import AtracaoSerializer

class PontoTuristicoSerializer(ModelSerializer):
    atracoes = AtracaoSerializer(many=True)
    class Meta:
        model = PontoTuristico
        fields = ['id','nome', 'descricao', 'aprovado', 'atracoes', 'comments', 'avaliacoes', 'localizacao','foto','atracoes']