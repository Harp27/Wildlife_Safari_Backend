from django.db import models

# Create your models here.
class Animal(models.Model):
    species_name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    habitat = models.CharField(max_length=200)
    conservation_status = models.CharField(max_length=200)
    population = models.CharField(max_length=200)
    image = models.CharField(max_length=200)

    