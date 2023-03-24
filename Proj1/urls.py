
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('',include('app1.urls'), name="home"),
    path('add',include('app1.urls'),name='add'),
    path('multiply',include('app1.urls'),name='multiply'),
    path('admin/', admin.site.urls),
]
