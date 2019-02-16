""" Models for cat collectr
"""
from django.db import models

# Create your models here.
class Cat(models.Model):
    """ Cats have name, breed, description, age (int) 
    the __str__ method returns name
    """

    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    age = models.IntegerField()

    def __str__(self):
        return self.name
