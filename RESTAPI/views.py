from django.shortcuts import render
from django.db import connection
from django.db.models import Q

# Create your views here.
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
# from .serializers import *
from rest_framework import status
from django.http import HttpResponse, JsonResponse
from rest_framework.renderers import JSONRenderer

import io
import json


def getCode(component):
    with connection.cursor() as cursor:
        codequery = "SELECT s FROM planes1 WHERE p = 'asignatura' AND o LIKE '" + component + "'"
        print(codequery)
        cursor.execute(codequery)
        row = cursor.fetchone()
        if row:
            code = row[0]
            print("CODIGO= " + code)
        else:
            code = ""
    return code


class CreditsComponent1(APIView):
    def get(self, request, component):
        code = getCode(component)
        print(code)
        creditsquery = Planes.objects.values('o').filter(p='creditos', s=code)
        print(creditsquery)
        if len(creditsquery)> 0:
            return Response(creditsquery,status=status.HTTP_200_OK)
        else:
            data =[{'o': 'No encuentro esta materia'}]
            return Response(data ,status=status.HTTP_400_BAD_REQUEST)


class CreditsComponent(APIView):
    def get(self, request, component):
        with connection.cursor() as cursor:
            code = getCode(component)
            print(code)
            data = []
            if code:
                creditsquery = "SELECT o FROM planes1 WHERE p = 'creditos' AND s = '" + code + "'"
                cursor.execute(creditsquery)
                row = cursor.fetchone()
                credits = row[0] + " ECTS"
                data.append({'answer': credits})
            else:
                data.append({'answer': 'No he encontrado la asignatura. Inténtalo nuevamente'})
        return Response(data)


class TitulacionComponent(APIView):
    def get(self, request, component):
        code = getCode(component)
        print(code)
        titulacionquery = Planes.objects.values('o').filter(p='responsable', s=code)
        print(titulacionquery)
        if len(titulacionquery) > 0:
            return Response(titulacionquery, status=status.HTTP_200_OK)
        else:
            data = [{'o': 'No encuentro esta materia'}]
            return Response(data, status=status.HTTP_400_BAD_REQUEST)

class TipoComponent(APIView):
    def get(self, request, component):
        code = getCode(component)
        print(code)
        tipoquery = Planes.objects.values('o').filter(p='grupo_creditos', s=code)
        print(tipoquery)
        if len(tipoquery) > 0:
            return Response(tipoquery, status= status.HTTP_200_OK)
        else:
            data = [{'o': 'No encuentro esta materia'}]
            return Response(data, status=status.HTTP_400_BAD_REQUEST)


class SeccionComponent(APIView):
    def get(self, request, component):
        code = getCode(component)
        print(code)
        seccionquery = Planes.objects.values('o').filter(p='seccion', s=code)
        print(seccionquery)
        if len(seccionquery) > 0:
            return Response(seccionquery, status=status.HTTP_200_OK)
        else:
            data = [{'o': 'No encuentro esta materia'}]
            return Response(data, status=status.HTTP_400_BAD_REQUEST)


class DepartamentoComponent(APIView):
    def get(self, request, component):
        code = getCode(component)
        print(code)
        departamentoquery = Planes.objects.values('o').filter(p='departamento', s=code)
        print(departamentoquery)
        if len(departamentoquery) > 0:
            return Response(departamentoquery, status=status.HTTP_200_OK)
        else:
            data = [{'o': 'No encuentro esta materia'}]
            return Response(data, status=status.HTTP_400_BAD_REQUEST)

class PeriodoComponent(APIView):
    def get(self, request, component):
        data = []
        code = getCode(component)
        print(code)
        periodoquery = Planes.objects.values('o').filter(p='periodo', s=code)
        cad = str(periodoquery[0]['o'])
        if cad.find("Oct"):
            data.append({'o': 'Ciclo impar: Octubre/Febrero'})
        else:
            data.append({'o': 'Ciclo par: Abril/Agosto'})

        if len(data) > 0:
            return Response(data, status=status.HTTP_200_OK)
        else:
            data = [{'o': 'No encuentro esta materia'}]
            return Response(data, status=status.HTTP_400_BAD_REQUEST)

class SubjectsListByRelatedWords(APIView):
    def get(self, request, component):
        if request.method == 'GET':
            with connection.cursor() as cursor:
                data = []
                codequery = "SELECT s FROM planes1 WHERE p = 'asignatura' AND o LIKE '" + component + "%'"
                cursor.execute(codequery)
                row = cursor.fetchone()
                code = row[0]
                data.append({'code': code})
        return Response(data)
