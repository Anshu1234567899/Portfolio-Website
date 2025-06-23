<<<<<<< HEAD
from django.db import models

# Create your models here.
class services(models.Model):
    services_icon=models.CharField(max_length=50)
    services_title=models.CharField(max_length=50)
    services_des=models.TextField()
    services_button_text = models.CharField(max_length=50)
    services_button_link = models.URLField(max_length=200)

    


=======
from django.db import models

# Create your models here.
class services(models.Model):
    services_icon=models.CharField(max_length=50)
    services_title=models.CharField(max_length=50)
    services_des=models.TextField()
    services_button_text = models.CharField(max_length=50)
    services_button_link = models.URLField(max_length=200)

    


>>>>>>> 876681c8413969cc389dd4e36e4c61eec798164f
