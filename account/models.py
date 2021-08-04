from django.db import models
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver
from django.urls import reverse
# Create your models here.

class User(AbstractUser):
    first_name = models.CharField(max_length=50, unique=True)
    last_name = models.CharField(max_length=50, unique=True)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=100 , unique=True)
    phone_no = models.CharField(max_length=10,blank=True, null=True)

    def __str__(self):
        return"{}".format(self.username)

class Restaurant(models.Model):
    r_name = models.CharField(max_length=100)
    r_contact = models.CharField(max_length=100)
    
    def __str__(self):
        return self.r_name

class Fooditem(models.Model):
    f_name = models.CharField(max_length=100)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    f_price = models.IntegerField()
    f_image = models.ImageField(upload_to = 'media')

    def __str__(self):
        return self.f_name

class Cart(models.Model):
    f_name = models.CharField(max_length=100)
    f_price = models.IntegerField()
    phoneno = models.CharField(max_length=100, default=None)
    address = models.CharField(max_length=100, default=None)