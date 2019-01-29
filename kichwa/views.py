from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, generics
from .serializers import *
from django.db.models import Q

# Create your views here.
class TiposList(generics.ListCreateAPIView):
    queryset = Tipos.objects.filter(~Q(castellano__startswith='Expresiones')).order_by('castellano')
    serializer_class = TiposSerializer

class GetType(generics.ListAPIView):
    serializer_class = TiposSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        idtipo = self.kwargs['id']
        return Tipos.objects.filter(id=idtipo)

class ExpresionesList(generics.ListCreateAPIView):
    queryset = Tipos.objects.filter(castellano__startswith='Expresiones')
    serializer_class = TiposSerializer


class WordsKichwasByCategory(generics.ListAPIView):
    serializer_class = ExpresionesSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        idcategory = self.kwargs['id']
        return Expresiones.objects.filter(tipo=idcategory)

class TranslateFromEnglish(generics.ListAPIView):
    serializer_class = MultilenguajeSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        word = self.kwargs['en']
        if len(word) > 3:
            query = Multilenguaje.objects.filter(english__icontains=word)
        else:
            query = Multilenguaje.objects.filter(english=word)
        return query


class TranslateFromKichwa(generics.ListAPIView):
    serializer_class = KichwaCastellanoSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        word = self.kwargs['kw']
        if len(word) > 3:
            query = KichwaCastellano.objects.filter(kichwa=word)
            if len(query) == 1:
                return query
            else:
                return KichwaCastellano.objects.filter(kichwa__icontains=word)[:3]
        else:
            query = KichwaCastellano.objects.filter(kichwa=word)
        return query


class TranslateFromEspanish(generics.ListAPIView):
    serializer_class = CastellanoKichwaSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        word = self.kwargs['es']
        if len(word) > 3:
            query = CastellanoKichwa.objects.filter(castellano=word)
            if len(query) == 1:
                return query
            else:
                query = CastellanoKichwa.objects.filter(castellano__icontains=word)[:3]
                if len(query) >= 1:
                    return query
                else:
                    #quering in other table
                    return KichwaCastellano.objects.filter(castellano__icontains=word)[:3]
        else:
            query = CastellanoKichwa.objects.filter(castellano=word)
        return query

class QueryInMultilenguaje(generics.ListAPIView):
    serializer_class = MultilenguajeSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        word = self.kwargs['es']
        if len(word) > 3:
            query = Multilenguaje.objects.filter(spanish=word)
            if len(query) == 1:
                return query
            else:
                return Multilenguaje.objects.filter(spanish__icontains=word)
        else:
            query = Multilenguaje.objects.filter(spanish=word)
        return query