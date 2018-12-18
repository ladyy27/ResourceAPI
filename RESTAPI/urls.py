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
]

