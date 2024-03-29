from rest_framework import generics

from .models import Curso, Aluno, Disciplina
from .serializers import CursoSerializer, CursoSerializerDetail, AlunoSerializer, AlunoSerializerDetail, DisciplinaSerializer


# Create your views here.
#----------Curso-----------------
class CursoList(generics.ListCreateAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

class CursoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializerDetail

#----------Aluno-----------------
class AlunoList(generics.ListCreateAPIView):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer


class AlunoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializerDetail

#----------Discplina-----------------
class DisciplinaList(generics.ListCreateAPIView):
    queryset = Disciplina.objects.all()
    serializer_class = DisciplinaSerializer


class DisciplinaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Disciplina.objects.all()
    serializer_class = DisciplinaSerializer