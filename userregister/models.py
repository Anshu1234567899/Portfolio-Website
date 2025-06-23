<<<<<<< HEAD
from django.db import models

gender_choices=[
        ('M','Male'),
        ('F','Female'),
        ('O','Other'),
        ]
class Userregister(models.Model):
    
    fullname=models.CharField(max_length=50)
    email=models.CharField(max_length=60)
    password=models.CharField(max_length=100)
    gender=models.CharField(max_length=1,choices=gender_choices)
=======
from django.db import models

gender_choices=[
        ('M','Male'),
        ('F','Female'),
        ('O','Other'),
        ]
class Userregister(models.Model):
    
    fullname=models.CharField(max_length=50)
    email=models.CharField(max_length=60)
    password=models.CharField(max_length=100)
    gender=models.CharField(max_length=1,choices=gender_choices)
>>>>>>> 876681c8413969cc389dd4e36e4c61eec798164f
