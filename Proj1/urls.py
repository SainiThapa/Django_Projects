
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('',include('Travello.urls'),name="index"),
    path('admin/', admin.site.urls),
]
