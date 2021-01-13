from rest_framework.viewsets import ModelViewSet
from pontos_turisticos.models import PontoTuristico
from .serializers import PontoTuristicoSerializer

class PontoTuristicoViewSet(ModelViewSet):
    #queryset = PontoTuristico.objects.all() #caso queira filtrar uma  busca se pode usar filter seguido pela condicao exemplo .filter(aprovados=true)
    def get_queryset(self):
        return PontoTuristico.objects.filter(aprovado=True)
    
    serializer_class =  PontoTuristicoSerializer