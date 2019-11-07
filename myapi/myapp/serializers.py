from rest_framework import serializers
from .models import Curso
from .models import Aluno

class CursoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Curso
        fields = '__all__'

class AlunoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Aluno
        fields = '__all__'