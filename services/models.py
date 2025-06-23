from django.db import models

# Create your models here.
class services(models.Model):
    services_icon=models.CharField(max_length=50)
    services_title=models.CharField(max_length=50)
    services_des=models.TextField()
    services_button_text = models.CharField(max_length=50)
    services_button_link = models.URLField(max_length=200)

    


