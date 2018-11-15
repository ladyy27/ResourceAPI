from .models import *
from rest_framework import serializers


class CursosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cursos
        fields = ['nombre']
