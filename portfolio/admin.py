
from django.contrib import admin
from django.contrib.admin.sites import site
from portfolio.models import portfolio

class portfolioAdmin(admin.ModelAdmin):
    list_display=('portfolio_title','portfolio_desc','portfolio_imag')

admin.site.register(portfolio,portfolioAdmin)
