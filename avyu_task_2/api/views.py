from rest_framework import mixins, viewsets

from . import models, serializers


class CardViewSet(mixins.ListModelMixin,
                  viewsets.GenericViewSet):
    """Вьюсет для карт"""
    queryset = models.Card.objects.all()
    serializer_class = serializers.CardsSerializer
