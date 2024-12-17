from django.db import models

class Institution (models.Model):
    name = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=14)

    def __str__(self):
        return f"{self.name} - {self.cnpj}"

