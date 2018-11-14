from . import views
from django.urls import path, re_path
from rest_framework.urlpatterns import format_suffix_patterns

from RESTAPI import views

urlpatterns = [
    #services
    re_path(r'^creditos/(?P<component>[-\w.]+(?: [-\w.]+)*)/', views.CreditsComponent.as_view()),
    #re_path(r'^rest/answer/(?P<intentname>[-\w.]+(?: [-\w.]+)*)/(?P<code>[-\w.]+(?: [-\w.]+)*)/', views.AnswerbyIntent.as_view()),
    #re_path(r'^articles/(?P<year>[0-9]{4})/$', views.year_archive),
]
