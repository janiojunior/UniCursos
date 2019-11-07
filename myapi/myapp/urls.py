from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^cursos/$', views.CursoList.as_view(), name='curso-list'),
    url(r'^curso/(?P<pk>[0-9]+)/$', views.CursoDetail.as_view(), name='curso-detail'),

    url(r'^alunos/$', views.AlunoList.as_view(), name='aluno-list'),
    url(r'^aluno/(?P<pk>[0-9]+)/$', views.AlunoDetail.as_view(), name='aluno-detail'),
]