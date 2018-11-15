from django.urls import path
from cursosHandler import views


urlpatterns = [
    path(r'todos/', views.listar_cursos, name='listar_cursos'),
    path(r'duracion/', views.duracion_curso, name='duracion_curso'),
    path(r'temas/', views.temas_curso, name='temas_curso'),
    path(r'profesor/', views.profesor_curso, name='profesor_curso'),
    path(r'info/', views.info_curso, name='info_curso'),
]
