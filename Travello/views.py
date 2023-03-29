from django.shortcuts import render
from .models import Destination

# Create your views here.

def index(request):
    dest1=Destination()
    dest1.name="Kathmandu"
    dest1.description="Land of Dreams"
    dest1.price="696"
    return render(request,"index.html",{'dest1':dest1})