from rest_framework import serializers
from kichwa.models import *


class MultilenguajeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Multilenguaje
        fields = ("kichwa", "english", "spanish", "speech", "category")


class TiposSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tipos
        fields = ("id", "castellano", "kichwa")


class KichwaCastellanoSerializer(serializers.ModelSerializer):
    class Meta:
        model = KichwaCastellano
        fields = ("kichwa", "phonema", "tipo", "toponimo", "sinonimos", "castellano")


class CastellanoKichwaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CastellanoKichwa
        fields = ("castellano", "tipo", "kichwa")


class ExpresionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expresiones
        fields = ("castellano", "kichwa")
