from django.http import JsonResponse
from rest_framework import viewsets

from . import serializers
from . import models


class GraphicViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.GraphicSerializer
    queryset = models.Graphic.objects.all()
