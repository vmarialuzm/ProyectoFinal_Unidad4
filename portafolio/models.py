from django.db import models

# Create your models here.

class usuario(models.Model):
    username=models.CharField(max_length=50,unique=True)
    password=models.CharField(max_length=50)
    
class datos_portafolio(models.Model):
    Foto = models.URLField()
    Título = models.CharField(max_length=50)
    Descripción = models.CharField(max_length=500)
    Tags = models.CharField(max_length=500)
    URL_github= models.URLField()

class Ip(models.Model):
    number_Ip=models.CharField(max_length=50)
    date=models.DateTimeField()
