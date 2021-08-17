from django.db import models

class Product(models.Model):
    name=models.CharField(max_length=100)
    brand = models.CharField(max_length=255)
    catagory= models.CharField(max_length=100)
    price = models.CharField(max_length=10)
    discription = models.CharField(max_length=300)
    

    
    rate = models.FloatField(max_length=100)
    status = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Busy_product(models.Model):
    quantity = models.IntegerField()