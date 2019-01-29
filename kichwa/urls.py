from django.urls import path
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from kichwa import views


urlpatterns = [
    path('typesexpressions/', views.TiposList.as_view()),
    path('expressions/', views.ExpresionesList.as_view()),
    url('^type/(?P<id>.+)/$', views.GetType.as_view()),
    url('^wordskichwas/(?P<id>.+)/$', views.WordsKichwasByCategory.as_view()),
    url('^fromenglish/(?P<en>.+)/$', views.TranslateFromEnglish.as_view()),
    url('^fromkichwa/(?P<kw>.+)/$', views.TranslateFromKichwa.as_view()),
    url('^fromespanish/(?P<es>.+)/$', views.TranslateFromEspanish.as_view()),
    url('^fromespanishretry/(?P<es>.+)/$', views.QueryInMultilenguaje.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)