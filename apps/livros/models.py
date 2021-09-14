from django.db import models
from django.contrib.auth.models import User

class Autor(models.Model):
    SEXO = (
        (1, 'Masculino'),
        (2, 'Feminino')
    )

    nome = models.CharField(max_length=150)
    data_nasc = models.DateField()
    nacionalidade = models.CharField(max_length=50)
    sexo = models.IntegerField(choices=SEXO)

    def __str__(self):
        return self.nome

class Editora(models.Model):
    nome = models.CharField(max_length=150)
    cidade = models.CharField(max_length=150)
    estado = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Livro(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=50)
    genero = models.CharField(max_length=50)
    qtd_paginas = models.IntegerField()
    ano_pub = models.IntegerField()
    resenha = models.TextField()
    autor = models.ManyToManyField(Autor)
    editora = models.ForeignKey(Editora, on_delete=models.CASCADE)
    publicado = models.BooleanField(default=False)
    capa_livro = models.ImageField(upload_to='capas/%d/%m/%Y', blank=True)

    def __str__(self):
        return self.nome

