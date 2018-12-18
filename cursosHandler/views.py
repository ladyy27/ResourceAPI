from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import *


# Create your views here.
@api_view(['GET'])
def listar_cursos(request):
    """
    Listar todos los cursos
    :param request:
    :return: EL nombre de los cursos
    """
    if request.method == 'GET':
        resp = Cursos.objects.values("nombre").all()
        return Response(resp, status=status.HTTP_200_OK)


@api_view(['GET'])
def duracion_curso(request):
    """
    Duracion del curso
    :param request: nombre del curso
    :return: Duracion del curso
    """
    if request.method == 'GET':
        serializer = CursosSerializer(data=request.data)
        if serializer.is_valid():
            query = Cursos.objects.values("nombre", "duracion", "esfuerzo_estimado").get(
                nombre__contains=serializer.validated_data["curso"])
            if len(query) == 0:
                return Response({"error": "Curso no encontrado"}, status=status.HTTP_404_NOT_FOUND)
            else:
                return Response(query, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def temas_curso(request):
    """
    Contenidos del curso
    :param request: nombre del curso
    :return: Contenidos del curso ordenados
    """
    if request.method == 'GET':
        serializer = CursosSerializer(data=request.data)
        if serializer.is_valid():
            query = Cursos.objects.values("nombre", "contenidos__contenido").filter(
                nombre__contains=serializer.validated_data["curso"]).order_by("contenidos__orden")
            contenidos = list(map(lambda x: x["contenidos__contenido"], query))
            if len(query) == 0:
                return Response({"error": "Curso no encontrado"}, status=status.HTTP_404_NOT_FOUND)
            else:
                resp = {"nombre": query[0]["nombre"],
                        "contenidos": contenidos}
                return Response(resp, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def profesor_curso(request):
    """
    Profesor encargado del curso
    :param request: nombre del curso
    :return: profesor del curso
    """
    if request.method == 'GET':
        serializer = CursosSerializer(data=request.data)
        if serializer.is_valid():
            query = Cursos.objects.values("nombre", "docentes__nombre").filter(
                nombre__contains=serializer.validated_data["curso"])
            print(query)
            if len(query) >= 2:
                docentes = list(map(lambda x: x["docentes__nombre"], query))
                resp = {"nombre": query[0]["nombre"],
                        "docentes": docentes}
                return Response(resp, status=status.HTTP_200_OK)
            elif len(query) == 0:
                return Response({"error": "Curso no encontrado"}, status=status.HTTP_404_NOT_FOUND)
            else:
                return Response(query, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def info_curso(request):
    """
    Informacion del curso
    :param request: nombre del curso
    :return: profesor del curso
    """
    if request.method == 'GET':
        serializer = CursosSerializer(data=request.data)
        if serializer.is_valid():
            try:
                query = Cursos.objects.values("nombre", "descripcion").get(
                    nombre__contains=serializer.validated_data["curso"])
                print(query)
            except Cursos.DoesNotExist:
                return Response({"error": "Curso no encontrado"}, status=status.HTTP_404_NOT_FOUND)
            else:
                resp = {"nombre": query["nombre"],
                        "descripcion": query["descripcion"]}
                return Response(resp, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
