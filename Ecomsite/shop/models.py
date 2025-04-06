from django.db import models

# Create your models here.
class Products(models.Model):
    title = models.CharField(max_length=200)
    price = models.FloatField()
    discountPrice =models.FloatField()
    category = models.CharField(max_length=200)
    description = models.TextField()
    image = models.CharField(max_length=300)


class order(models.Model):
    item = models.CharField(max_length=1000)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=300)
    address = models.CharField(max_length=500)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=50)
    total = models.CharField(max_length=100)