from django.urls import path
# from django.contrib import admin
from . import views

urlpatterns=[
    path('',views.home,name ='home'),
    path('add',views.add,name ='add'),
    path('multiply',views.mul,name ='multiply'),
    
    ]