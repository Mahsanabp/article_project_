from django.db import models
import os
import random

# Create your models here.



def upload_image_path(instance, filename):
    ext = os.path.splitext(filename)[1]
    random_number = str(random.randint(10000000, 999999999))
    return f"articles/article-image-{random_number}{ext}"


class Article(models.Model):
    name = models.CharField(max_length=300)
    rate = models.IntegerField()
    date = models.DateField()
    link = models.TextField()
    image = models.ImageField(upload_to=upload_image_path)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name = "article"  #with s
        verbose_name_plural = "article List"  #without s