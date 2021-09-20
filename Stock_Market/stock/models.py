from django.db import models
from django.db.models.base import Model
from django.urls import reverse

class Product(models.Model):
    name=models.CharField(max_length=100)
    brand = models.CharField(max_length=255)
    catagory= models.CharField(max_length=100)
    price = models.CharField(max_length=10)
    discription = models.CharField(max_length=300)
    rate = models.FloatField(max_length=100)
    status = models.CharField(max_length=10)
    slug=models.SlugField(max_length=40)

    def __str__(self):
        return self.name
    
    

class Busy_product(models.Model):
    quantity = models.IntegerField()
    report=models.ForeignKey(Product,on_delete=models.CASCADE)