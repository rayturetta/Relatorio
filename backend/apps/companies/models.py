from django.db import models
from ..institutions.models import Institution

KIND_CHOICES = {
    "MATRIZ": "MATRIZ",
    "FILIAL": "FILIAL",
}

NATURE_LEGAL_CHOICES = {
    "FAZER": "FAZER",
}

REGIME_CHOICES = {
    "PRESUMIDO": "Lucro Presumido",
    "REAL": "Lucro Real",
    "SIMPLES": "Simples Nacional",
    "SIMEI": "SIMEI",
}

RESPONSIBILITY_CHOICES = {
    "FAZER": "FAZER",
}

SITUATION_CHOICES = {
    "ATIVO": "ATIVO",
    "INATIVO": "INATIVO",
}

SIZE_CHOICES = {
    "GRANDE": "Empresa de Grande Porte",
    "MÉDIO": "Empresa de Médio Porte",
    "EPP": "Empresa de Pequeno Porte (EPP)",
    "ME": "Microempresa",
    "MEI": "Micro Empreendedor Individual (MEI)",
}


class Activity (models.Model):
    code = models.CharField(max_length=7)
    description =  models.CharField()

    class Meta:
        db_table = "activities"

    def __str__(self):
        return f"{ self.code } - { self.description}"


class Contact (models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = "contacts"

    def __str__(self):
        return self.name


class Society (models.Model):
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    responsibility = models.CharField(RESPONSIBILITY_CHOICES)

    class Meta:
        db_table = "societies"

    def __str__(self):
        return f"{ self.responsibility } - { self.contact}"


class Company (models.Model):
    name = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=14)
    constitution = models.DateField()
    kind = models.CharField(KIND_CHOICES)
    social_capital = models.DecimalField(decimal_places=2)
    primary_activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    secondary_activity = models.ManyToManyField(Activity, on_delete=models.CASCADE)
    regime = models.CharField(max_length=7, choices=REGIME_CHOICES)
    size = models.CharField(max_length=7, choices=SIZE_CHOICES)
    state = models.CharField(max_length=2)
    zip_code = models.CharField(max_length=8)
    nature_legal = models.CharField(choices=NATURE_LEGAL_CHOICES)
    society = models.ForeignKey(Society, on_delete=models.CASCADE)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    situation = models.CharField(max_length=7)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "companies"

    def __str__(self):
        return f"{ self.name } - { self.cnpj}"




