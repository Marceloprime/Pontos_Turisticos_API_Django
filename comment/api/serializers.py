from comment.models import Comentario
from rest_framework.serializers import ModelSerializer


class ComentarioSerializer(ModelSerializer):
    class Meta:
        model = Comentario
        fields = ['usuario', 'descricao', 'date', 'aprovado']