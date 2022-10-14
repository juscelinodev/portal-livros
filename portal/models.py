from unittest.util import _MAX_LENGTH
from django.db import models
# Create your models here.
class Autor(models.Model):
    nome = models.CharField(max_length=255)
    data_nascimento = models.DateField()
    email = models.EmailField()

class Livro(models.Model):
    titulo = models.CharField(max_length=255)
    subtitulo = models.CharField(max_length=255, blank=True, null=True)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    data_lancamento = models.DateField()
    isbn = models.CharField(max_length=255)
    numero_paginas = models.PositiveBigIntegerField()