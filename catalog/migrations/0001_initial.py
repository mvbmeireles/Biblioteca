# Generated by Django 3.2.3 on 2021-05-25 17:24

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('primeiro_nome', models.CharField(max_length=100)),
                ('último_nome', models.CharField(max_length=100)),
                ('data_de_nascimento', models.DateField(blank=True, null=True)),
                ('data_da_morte', models.DateField(blank=True, null=True, verbose_name='Died')),
            ],
            options={
                'ordering': ['primeiro_nome', 'último_nome'],
            },
        ),
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(help_text='Gênero do livro (Romance, Biografia, etc.)', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Livro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('título', models.CharField(max_length=200)),
                ('sumário', models.TextField(help_text='Breve descrição do livro', max_length=1000)),
                ('isbn', models.CharField(max_length=13, unique=True, verbose_name='ISBN')),
                ('autor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.autor')),
                ('gênero', models.ManyToManyField(help_text='Gênero do livro (Romance, Biografia, etc.)', to='catalog.Genero')),
            ],
        ),
        migrations.CreateModel(
            name='EstadoDoLivro',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='ID único para cada livro na biblioteca', primary_key=True, serialize=False)),
                ('versão', models.CharField(max_length=200)),
                ('devolução', models.DateField(blank=True, null=True)),
                ('status', models.CharField(blank=True, choices=[('e', 'Emprestado'), ('d', 'Disponível'), ('r', 'Reservado')], default='d', help_text='Disponibilidade do livro', max_length=1)),
                ('livro', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='catalog.livro')),
            ],
            options={
                'ordering': ['devolução'],
            },
        ),
    ]
