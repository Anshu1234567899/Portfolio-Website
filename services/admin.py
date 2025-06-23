<<<<<<< HEAD
from django.contrib import admin
from services.models import services
# Register your models here.
class ServiceAdmin(admin.ModelAdmin):
    list_display=('services_icon','services_title','services_des')

=======
from django.contrib import admin
from services.models import services
# Register your models here.
class ServiceAdmin(admin.ModelAdmin):
    list_display=('services_icon','services_title','services_des')

>>>>>>> 876681c8413969cc389dd4e36e4c61eec798164f
admin.site.register(services,ServiceAdmin)