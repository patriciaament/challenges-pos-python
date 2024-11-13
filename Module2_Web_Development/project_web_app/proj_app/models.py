from django.db import models

class User(models.Model):
    nome = models.CharField('nome', max_length=30)

    def __str__(self):
        return f"Nome: {self.nome}"