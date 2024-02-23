"""
URL configuration for fortune project.
"""
from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path

from fortune import views

urlpatterns = [
    path('', lambda req: redirect('/today/')),
    path('admin/', admin.site.urls),
    path('today/', views.get_fortune, name='today_fortune')
]
