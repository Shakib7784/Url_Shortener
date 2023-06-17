from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path("",views.home,name="home"),
    path("<str:shortest_part>",views.redirect_url,name="redirect")
    
]