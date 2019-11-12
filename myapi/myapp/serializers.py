from rest_framework import serializers
from .models import Curso, Aluno, Disciplina

class CursoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Curso
        fields = '__all__'

class CursoSerializer2(serializers.ModelSerializer):

    class Meta:
        model = Curso
        fields = ['id', 'nome', 'cidade', 'total_pontos']

class AlunoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Aluno
        fields = '__all__'

class AlunoSerializerDetail(serializers.ModelSerializer):
    cursos = CursoSerializer2(many=True)

    class Meta:
        model = Aluno
        fields = ['id', 'nome', 'cpf', 'cursos']

class DisciplinaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Disciplina
        fields = ['nome']


class DisciplinaSerializer2(serializers.ModelSerializer):

    class Meta:
        model = Disciplina
        fields = ['id', 'nome']

class CursoSerializerDetail(serializers.ModelSerializer):
    disciplinas = DisciplinaSerializer2(many=True)

    class Meta:
        model = Curso
        fields = ['id', 'nome', 'cidade', 'disciplinas']