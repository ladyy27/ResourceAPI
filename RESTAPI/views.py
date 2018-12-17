from django.shortcuts import render
from django.db import connection
from django.db.models import Q

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from rest_framework import status
from django.http import HttpResponse, JsonResponse
from rest_framework.renderers import JSONRenderer

import io
import json

class Coincidentes(APIView):
    def get(self, request, component):
        print(component)
        asignatura = 'asignatura'
        #query1 = Planes.objects.filter(p = asignatura).values()
        query = Planes.objects.filter(o__startswith= component).values()
        #query = Planes.objects.raw('SELECT * FROM planes1 WHERE p = %s and o LIKE %s',[asignatura,component])
        print(query)
        return Response(query)

def getCode(component):
    with connection.cursor() as cursor:
        codequery = "SELECT s FROM planes1 WHERE p = 'asignatura' AND o LIKE '" + component + "'"
        print (codequery)
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
                codequery = "SELECT s FROM planes1 WHERE p = 'asignatura' AND o LIKE '"+ component +"%'"
                cursor.execute(codequery)
                row = cursor.fetchone()
                code = row[0]
                data.append({'code': code})
        return Response(data)


class AnswerbyIntent(APIView):
    def get(self, request, intentname, code):
        with connection.cursor() as cursor:
            intentId = Intent.objects.values('id').get(intentname=intentname)

            if intentId['id'] == 1 :
                answer= "SELECT a.answerTemplate, p.o FROM answer a, planes1 p WHERE a.intentId = 1 and  p.s = '" + code + "'and p.p = 'creditos' "
            elif intentId['id'] == 2:
                answer = "SELECT a.answerTemplate, p.o * 32 FROM answer a, planes1 p WHERE a.intentId = 2 and  p.s = '" + code + "'and p.p = 'creditos' "
            elif intentId['id'] == 5:
                answer = "SELECT a.answerTemplate, p.o FROM answer a, planes1 p WHERE a.intentId = 5 and  p.s = '" + code + "'and p.p = 'seccion' "
            elif intentId['id'] == 4:
                preanswer = "SELECT o FROM planes1 WHERE s = '" + code + "' and p = 'periodo'"
                cursor.execute(preanswer)
                row = cursor.fetchone()
                if str(row[0]).find('Oct') != -1:
                    answer = "SELECT answerTemplate FROM answer WHERE id = 4 and intentId = 4"
                else:
                    answer = "SELECT answerTemplate FROM answer WHERE id = 9 and intentId = 4"

            cursor.execute(answer)
            row = cursor.fetchone()
            print (row)
            if len (row) > 1:
                a = str(row[0])
                v = str(row[1])
                if a.find('?') != -1:
                    c = a.replace('?', v)
                    print (c)

                c = a + " " + v
                print (c)
            else:
                c = str(row[0])

            data = []
            data.append({'answer': c})
        return Response(data)
