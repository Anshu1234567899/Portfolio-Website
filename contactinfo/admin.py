<<<<<<< HEAD
from django.contrib import admin
from django.contrib.admin.sites import site
from contactinfo.models import Contactinfo

class ContactinfoAdmin(admin.ModelAdmin):
    list_display=('name','email','message')

=======
from django.contrib import admin
from django.contrib.admin.sites import site
from contactinfo.models import Contactinfo

class ContactinfoAdmin(admin.ModelAdmin):
    list_display=('name','email','message')

>>>>>>> 876681c8413969cc389dd4e36e4c61eec798164f
admin.site.register(Contactinfo,ContactinfoAdmin)