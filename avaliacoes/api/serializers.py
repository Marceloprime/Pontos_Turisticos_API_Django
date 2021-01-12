from avaliacoes.models import Avaliacao
from rest_framework.serializers import ModelSerializer


class AvaliacaoSerializer(ModelSerializer):
    class Meta:
        model = Avaliacao
        fields = ['user', 'comentario', 'nota', 'date']