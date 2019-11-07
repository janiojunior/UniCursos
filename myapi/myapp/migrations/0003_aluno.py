# Generated by Django 2.2.7 on 2019-11-07 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20191107_1753'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=60)),
                ('cpf', models.CharField(max_length=14)),
                ('senha', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'aluno',
            },
        ),
    ]
