from django.db import models

# Create your models here.
class Persona(models.Model):
    name = models.TextField(max_length=150, default="Some string")
    address = models.TextField(max_length=150, default="Some string")
    productType = models.TextField(max_length=150, default="Some string")
    email = models.TextField(max_length=150, default="Some string")
    garantia = models.TextField(max_length=150, default="Some string")
    marca = models.TextField(max_length=150, default="Some string")
    number = models.TextField(max_length=150, default="Some string")
    danio = models.TextField(max_length=150, default="Some string")
    time = models.TextField(max_length=150, default="Some string")
    