from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request,'home.html',{'name':'Saini'})

def add(request):
    val1=request.GET['num1']
    val2=request.GET['num2']
    res=int(val1)+int(val2)
    return render(request,'result.html',{'result':res})

def mul(request):
    val1=int(request.POST['num1'])
    val2=int(request.POST['num2'])
    res=(val1)*(val2)
    return render(request,'result.html',{'result':res})