from atracoes.models import Atracao
from rest_framework.serializers import ModelSerializer


class AtracaoSerializer(ModelSerializer):
    class Meta:
        model = Atracao
        fields = ['nome', 'descricao', 'horario', 'idade_min','foto']