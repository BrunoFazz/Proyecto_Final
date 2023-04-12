from django.db import models

# Create your models here.
class Filial(models.Model):
    nombre = models.CharField(max_length=20)
    sede = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.id} - {self.nombre} - {self.sede}"