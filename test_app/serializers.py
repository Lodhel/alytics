from rest_framework import serializers
from . import models


class GraphicSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Graphic

        fields = "__all__"
