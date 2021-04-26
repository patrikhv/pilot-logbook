from django.db import models

class SimpleModel(models.Model):
    """ Example of model """
    dummy = models.CharField(max_length=64, default="I am simple model !")

