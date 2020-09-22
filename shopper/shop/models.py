from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.



class Products(models.Model):
    
    image = models.ImageField(default='default.jpg' , upload_to='product_picure')
    desc = models.TextField(null=True)
    price = models.BigIntegerField()
    title = models.CharField(max_length=100)





class Purchase(models.Model):
    
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    p_id = models.ForeignKey(Products , on_delete=models.CASCADE)
    time_purchased = models.DateTimeField(default=timezone.now)
    

