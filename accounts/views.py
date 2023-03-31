from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth

# Create your views here.

def register(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        Username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']

        if(password1==password2):
            if User.objects.filter(username=Username).exists():
                print('Username already taken')
            elif User.objects.filter(email=email).exists():
                print('Email already in use')
            else:
                user=User.objects.create_user(username=Username,password=password1, email=email,first_name=first_name,last_name=last_name)
                user.save();
                print('USER CREATED !')
        else:
            print("Password doesnot match")
        return redirect('/')
    else:
        return render(request,'register.html')