from django.db import models
from django.urls import reverse
import uuid

# Create your models here.

class Genero(models.Model):
    nome = models.CharField(
        max_length=200,
        help_text="Gênero do livro (Romance, Biografia, etc.)"
        )

    def __str__(self):
        return self.nome

class Livro(models.Model):
    título = models.CharField(max_length=200)
    autor = models.ForeignKey('Autor', on_delete=models.SET_NULL, null=True)
    sumário = models.TextField(max_length=1000, help_text="Breve descrição do livro")
    isbn = models.CharField('ISBN', max_length=13,
                            unique=True
                            )
    gênero = models.ManyToManyField(Genero, help_text="Gênero do livro (Romance, Biografia, etc.)")

class Informações(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='ID único para cada livro na biblioteca')
    livro = models.ForeignKey('Livro', on_delete=models.RESTRICT, null=True)
    versão = models.CharField(max_length=200)
    devolução = models.DateField(null=True, blank=True)

    EMPRESTIMO = (
        ('e', 'Emprestado'),
        ('d', 'Disponível'),
        ('r', 'Reservado'),
    )

    status = models.CharField(
        max_length=1,
        choices=EMPRESTIMO,
        blank=True,
        default='d',
        help_text='Disponibilidade do livro',
    )

    class Meta:
        ordering = ['devolução']

    def __str__(self):
        return f'{self.id} ({self.livro.título})'

class Autor(models.Model):
    primeiro_nome = models.CharField(max_length=100)
    último_nome = models.CharField(max_length=100)
    data_de_nascimento = models.DateField(null=True, blank=True)
    data_da_morte = models.DateField('Died', null=True, blank=True)

    class Meta:
        ordering = ['primeiro_nome', 'último_nome']

    def get_absolute_url(self):
        return reverse('detalhes-do-autor', args=[str(self.id)])

    def __str__(self):
        return f'{self.último_nome}, {self.primeiro_nome}'