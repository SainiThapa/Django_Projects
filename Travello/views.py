from django.shortcuts import render
from .models import Destination

# Create your views here.

def index(request):

    # dest4=Destination()
    # dest4.name="Bardiya"
    # dest4.description="The home of the Tigers"
    # dest4.price="699"
    # dest4.img="Bardiya.jpg"
    # dest4.offer=False

    # dest5=Destination()
    # dest5.name="Butwal"
    # dest5.description="Learning through practice"
    # dest5.price="659"
    # dest5.img="Butwal.jpg"
    # dest5.offer=False
    
    # dest6=Destination()
    # dest6.name="Mustang"
    # dest6.description="The Forbidden Kingdom"
    # dest6.price="599"
    # dest6.img="Mustang.jpeg"
    # dest6.offer=True
    
    dests=Destination.objects.all()
    return render(request,"index.html",{'dests':dests})