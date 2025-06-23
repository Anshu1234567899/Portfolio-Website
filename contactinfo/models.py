<<<<<<< HEAD
from django.db import models

# Create your models here.
class Contactinfo(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=60)
    message=models.TextField()
=======
from django.db import models

# Create your models here.
class Contactinfo(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=60)
    message=models.TextField()
>>>>>>> 876681c8413969cc389dd4e36e4c61eec798164f
