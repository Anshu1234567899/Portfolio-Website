from django.contrib import admin
from django.contrib.admin.sites import site
from userregister.models import Userregister

class UserregisterAdmin(admin.ModelAdmin):
    list_display=('fullname','email','password','gender')

admin.site.register(Userregister,UserregisterAdmin)

