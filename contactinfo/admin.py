from django.contrib import admin
from django.contrib.admin.sites import site
from contactinfo.models import Contactinfo

class ContactinfoAdmin(admin.ModelAdmin):
    list_display=('name','email','message')

admin.site.register(Contactinfo,ContactinfoAdmin)