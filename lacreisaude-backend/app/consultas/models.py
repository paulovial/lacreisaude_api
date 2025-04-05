from django.db import models


class Profissional(models.Model):
    nome_social = models.CharField(max_length=255)
    profissao = models.CharField(max_length=255)
    endereco = models.CharField(max_length=255)
    contato = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.nome_social} ({self.profissao})"


class Consulta(models.Model):
    data = models.DateTimeField()
    profissional = models.ForeignKey(Profissional, on_delete=models.CASCADE, related_name="consultas")

    def __str__(self):
        return f"Consulta com {self.profissional.nome_social} em {self.data}"

