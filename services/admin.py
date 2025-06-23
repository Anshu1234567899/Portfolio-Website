from django.contrib import admin
from services.models import services
# Register your models here.
class ServiceAdmin(admin.ModelAdmin):
    list_display=('services_icon','services_title','services_des')

admin.site.register(services,ServiceAdmin)