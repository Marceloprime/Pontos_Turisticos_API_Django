from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from pontos_turisticos.models import PontoTuristico
from .serializers import PontoTuristicoSerializer
from rest_framework.decorators import action
import django_filters.rest_framework


class PontoTuristicoViewSet(ModelViewSet):
    queryset = PontoTuristico.objects.all() #caso queira filtrar uma  busca se pode usar filter seguido pela condicao exemplo .filter(aprovados=true)
    serializer_class =  PontoTuristicoSerializer

    def get_queryset(self):
        return PontoTuristico.objects.filter(aprovado=True) #retornar so os aprovados
  
    def list(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).create(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).destroy(request, *args, **kwargs)

    @action(methods=['post','get'], detail=False)
    def denuciar(self, request,pk=None):
        return Response({'status': 'password set'})
