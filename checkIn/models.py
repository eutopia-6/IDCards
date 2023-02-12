from django.db import models

# Create your models here.

class idcard(models.Model):
    name = models.CharField(max_length=60)
    height_cm = models.IntegerField(default=0)
    weight_ib = models.IntegerField(default=0)
    eye_color = models.CharField(max_length=10)
    image = models.ImageField(upload_to='images', default=None)

class users(models.Model):
    username = models.CharField(max_length=12)
    password = models.CharField(max_length=20)

class chat(models.Model):
    text_field = models.TextField(max_length=1000)
    author = models.CharField(max_length=12)
