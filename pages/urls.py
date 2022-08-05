from importlib.resources import path
from unicodedata import name
from django.contrib import admin
from . import views
from django.urls import path

urlpatterns = [
    path('', views.index,name="index"),
    path('about', views.about,name="about"),
    
]
