from django.db import models
from tinymce.models import HTMLField
from django.utils.text import slugify

class portfolio(models.Model):  
    portfolio_title = models.CharField(max_length=100)
    portfolio_desc = HTMLField()
    portfolio_imag=models.FileField(upload_to="portfolio/",max_length=250,null=True,default=None)
    portfolio_slug = models.SlugField(unique=True, null=True, default=None)

