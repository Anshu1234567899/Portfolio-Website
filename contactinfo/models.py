from django.db import models

# Create your models here.
class Contactinfo(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=60)
    message=models.TextField()

