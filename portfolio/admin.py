<<<<<<< HEAD
from django.contrib import admin
from django.contrib.admin.sites import site
from portfolio.models import portfolio

class portfolioAdmin(admin.ModelAdmin):
    list_display=('portfolio_title','portfolio_desc','portfolio_imag')

admin.site.register(portfolio,portfolioAdmin)
=======
from django.contrib import admin
from django.contrib.admin.sites import site
from portfolio.models import portfolio

class portfolioAdmin(admin.ModelAdmin):
    list_display=('portfolio_title','portfolio_desc','portfolio_imag')

admin.site.register(portfolio,portfolioAdmin)
>>>>>>> 876681c8413969cc389dd4e36e4c61eec798164f
