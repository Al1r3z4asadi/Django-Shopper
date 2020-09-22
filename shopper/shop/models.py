from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils import timezone
from PIL import Image


# Create your models here.



class Products(models.Model):
    
    image = models.ImageField(default='default.jpg' , upload_to='product_picure')
    desc = models.TextField(null=True)
    price = models.BigIntegerField()
    title = models.CharField(max_length=100)
    purchase_id = models.ForeignKey('Purchase' , on_delete = models.CASCADE , null = True , blank=True)



    def __str__(self):
        return self.title

    
    def save(self , *args , **kwargs):
        super().save(*args , **kwargs)
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300 :
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)



    
class Purchase(models.Model):
    
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    time_purchased = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.user_id.username

