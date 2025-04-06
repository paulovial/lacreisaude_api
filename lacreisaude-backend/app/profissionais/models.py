from django.db import models

class Profissional(models.Model):
    nome_social = models.CharField(max_length=255)
    profissao = models.CharField(max_length=255)
    endereco = models.CharField(max_length=255)
    contato = models.CharField(max_length=255)
