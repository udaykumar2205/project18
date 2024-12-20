from django.db import models

# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=100)
    population = models.IntegerField()  
    area = models.FloatField()  
    continent = models.CharField(max_length=50)  

    

class Capital(models.Model):
    country = models.OneToOneField(Country, on_delete=models.CASCADE) 
    name = models.CharField(max_length=100)
    population = models.IntegerField()  
    area = models.FloatField()
