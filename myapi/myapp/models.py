from django.db import models

# Create your models here.

class Curso(models.Model):
    class Meta:
        db_table = 'curso'

    nome = models.CharField(max_length=60)
    cidade = models.CharField(max_length=60)
    total_pontos = models.IntegerField()
    aluno = models.ForeignKey('Aluno', related_name='cursos', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.nome

class Aluno(models.Model):
    class Meta:
        db_table = 'aluno'

    nome = models.CharField(max_length=60)
    cpf = models.CharField(max_length=14)
    senha = models.CharField(max_length=30)

    def __str__(self):
        return self.nome
