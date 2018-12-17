from .models import *
from rest_framework import serializers


class CursosSerializer(serializers.Serializer):
    curso = serializers.CharField(required=True, max_length=60)

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass
