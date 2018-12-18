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
        return Response(creditsquery)


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
        creditsquery = Planes.objects.values('o').filter(p='responsable', s=code)
        print(creditsquery)
        return Response(creditsquery)


class TipoComponent(APIView):
    def get(self, request, component):
        code = getCode(component)
        print(code)
        creditsquery = Planes.objects.values('o').filter(p='grupo_creditos', s=code)
        print(creditsquery)
        return Response(creditsquery)


class SeccionComponent(APIView):
    def get(self, request, component):
        code = getCode(component)
        print(code)
        creditsquery = Planes.objects.values('o').filter(p='seccion', s=code)
        print(creditsquery)
        return Response(creditsquery)


class DepartamentoComponent(APIView):
    def get(self, request, component):
        code = getCode(component)
        print(code)
        creditsquery = Planes.objects.values('o').filter(p='departamento', s=code)
        print(creditsquery)
        return Response(creditsquery)


class PeriodoComponent(APIView):
    def get(self, request, component):
        data = []
        code = getCode(component)
        print(code)
        creditsquery = Planes.objects.values('o').filter(p='periodo', s=code)
        cad = str(creditsquery[0]['o'])
        if cad.find("Oct"):
            data.append({'o': 'Ciclo impar: Octubre/Febrero'})
        else:
            data.append({'o': 'Ciclo par: Abril/Agosto'})
        return Response(data)


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
