"""
URL configuration for BharatBuilds project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from BharatBuilds import views 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('about/',views.about),
    path('skill/',views.skill),
    path('project/',views.project),
    path('contact/',views.contact),
    path('resources/',views.resources),
    path('info/',views.info),
    path('detail/',views.detail,name='detail'),
    path('calculator/',views.calculator,name='calculator'),
    path('registration/',views.registration),
    path('login/',views.login),
    path('evodd/',views.evodd),
    path('saveinfo/',views.saveinfo, name="saveinfo"),
    path('marksheet/',views.marksheet),
    path('portfoliodetails/<slug>',views.portfoliodetails),
    path('resources/<resourcesid>',views.resourcedetails),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)