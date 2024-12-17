from django.db import models
from ..institutions.models import Institution

class Agency (models.Model):
    name = models.CharField(max_length=100)
    number =  models.IntegerField(max_length=4)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)


