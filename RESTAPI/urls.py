from . import views
from django.urls import path, re_path
from rest_framework.urlpatterns import format_suffix_patterns

from RESTAPI import views

urlpatterns = [
    #services
    re_path(r'^creditos/(?P<component>[-\w.]+(?: [-\w.]+)*)/', views.CreditsComponent1.as_view()),
    re_path(r'^titulacion/(?P<component>[-\w.]+(?: [-\w.]+)*)/', views.TitulacionComponent.as_view()),
    re_path(r'^tipo/(?P<component>[-\w.]+(?: [-\w.]+)*)/', views.TipoComponent.as_view()),
    re_path(r'^seccion/(?P<component>[-\w.]+(?: [-\w.]+)*)/', views.SeccionComponent.as_view()),
    re_path(r'^departamento/(?P<component>[-\w.]+(?: [-\w.]+)*)/', views.DepartamentoComponent.as_view()),
    re_path(r'^periodo/(?P<component>[-\w.]+(?: [-\w.]+)*)/', views.PeriodoComponent.as_view()),
    re_path(r'^materias/(?P<component>[-\w.]+(?: [-\w.]+)*)/', views.Coincidentes.as_view()),
    #re_path(r'^creditos/(?P<component>[-\w.]+(?: [-\w.]+)*)/', views.CreditsComponentSerializers.as_view()),
    #re_path(r'^creditos/(?P<component>[-\w.]+(?: [-\w.]+)*)/', views.creditByMateria),
    #path(r'creditos/', views.listar_cursos, name='listar_cursos'),
    #re_path(r'^rest/answer/(?P<intentname>[-\w.]+(?: [-\w.]+)*)/(?P<code>[-\w.]+(?: [-\w.]+)*)/', views.AnswerbyIntent.as_view()),
    #re_path(r'^articles/(?P<year>[0-9]{4})/$', views.year_archive),
]


"""
urlpatterns = [
    path('snippets/', views.snippet_list),
    path('snippets/<int:pk>/', views.snippet_detail),
]
"""
