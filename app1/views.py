from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse('Hello World')

def add(request):
    return HttpResponse('5')