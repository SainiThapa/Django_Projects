from django.shortcuts import render
from .models import Destination

# Create your views here.

def index(request):
    dest1=Destination()
    dest1.name="Kathmandu"
    dest1.description="Land of Dreams"
    dest1.price="696"
    dest1.img="ktm.jpeg"
    
    dest2=Destination()
    dest2.name="Pokhara"
    dest2.description="Clean Pokhara, Green Pokhara"
    dest2.price="669"
    dest2.img="Pokhara.jpg"

    dest3=Destination()
    dest3.name="Butwal"
    dest3.description="Learning through practice"
    dest3.price="659"
    dest3.img="Butwal.jpg"

    dest4=Destination()
    dest4.name="Bardiya"
    dest4.description="The home of the Tigers"
    dest4.price="699"
    dest4.img="Bardiya.jpg"
    
    dest5=Destination()
    dest5.name="Chitwan"
    dest5.description="Home of the Rhinos"
    dest5.price="696"
    dest5.img="Chitwan.jpg"

    
    dest6=Destination()
    dest6.name="Mustang"
    dest6.description="The Forbidden Kingdom"
    dest6.price="599"
    dest6.img="Mustang.jpeg"

    
    
    dests=[dest1,dest2,dest3,dest4,dest5,dest6]
    return render(request,"index.html",{'dests':dests})