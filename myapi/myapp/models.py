from django.db import models
from datetime import datetime
# Create your models here.

class Disciplina(models.Model):
    class Meta:
        db_table = 'disciplina'
    nome = models.CharField(max_length=60)

    def __str__(self):
        return self.nome

class Curso(models.Model):
    class Meta:
        db_table = 'curso'

    nome = models.CharField(max_length=60)
    cidade = models.CharField(max_length=60)
    disciplinas = models.ManyToManyField(Disciplina)

    # campo calculado
    total_pontos = 0

    def __str__(self):
        return self.nome

class Aluno(models.Model):
    class Meta:
        db_table = 'aluno'

    nome = models.CharField(max_length=60)
    cpf = models.CharField(max_length=14)
    senha = models.CharField(max_length=30)
    cursos = models.ManyToManyField(Curso)

    def __str__(self):
        return self.nome

class Atividade(models.Model):
    class Meta:
        db_table = 'atividade'
    nome = models.CharField(max_length=60)
    disciplina = models.ForeignKey('Disciplina', related_name='atividades', on_delete=models.PROTECT,  null=False)
    # campos calculados
    porcentagem = 0
    total_pontos = 0

    def __str__(self):
        return self.nome

class Exercicio(models.Model):
    class Meta:
        db_table = 'exercicio'

    TIPO_PESO = (
        (1, "Fácil"),
        (2, "Médio"),
        (3, "Difícil"),
    )
    descricao = models.CharField(max_length=300)
    peso = models.IntegerField(max_length=1, choices=TIPO_PESO, blank=False, null=False)
    atividade = models.ForeignKey('Atividade', related_name='exercicios', on_delete=models.PROTECT,  null=False)

    def __str__(self):
        return self.descricao

class Alternativa(models.Model):
    class Meta:
        db_table = 'alternativa'
    descricao = models.CharField(max_length=200)
    verdadeiro = models.BooleanField(False)
    exercicio = models.ForeignKey('Exercicio', related_name='alternativas', on_delete=models.PROTECT,  null=False)

    def __str__(self):
        return self.descricao

class Resposta(models.Model):
    class Meta:
        db_table = 'resposta'
    data = models.DateTimeField(default=datetime.now, blank=False)
    aluno = models.ForeignKey('Aluno', related_name='respostas', on_delete=models.PROTECT,  null=False)
    exercicio = models.ForeignKey('Exercicio', related_name='respostas', on_delete=models.PROTECT,  null=False)
    alternativa = models.ForeignKey('Alternativa', related_name='respostas', on_delete=models.PROTECT,  null=False)

    def __str__(self):
        return self.data