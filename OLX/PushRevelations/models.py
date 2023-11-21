from django.db import models
from django.contrib.auth import get_user_model
from Catalog.models import Category
from slugify import slugify
# Create your models here.

class Revelation(models.Model):
    id = models.IntegerField(primary_key=True)
    category = models.ForeignKey(Category, related_name='revelations', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='gallery', null=True)
    image_2 = models.ImageField(upload_to='gallery', null=True)
    image_3 = models.ImageField(upload_to='gallery', null=True)




class Gallery(models.Model):

    Revelation = models.ForeignKey(Revelation, on_delete=models.CASCADE, related_name='images')