from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)
    avatar = models.ImageField(upload_to="images/")
    slug = models.SlugField(max_length=200)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name