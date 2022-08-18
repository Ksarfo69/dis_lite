from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'homepage.html')

def rooms(request):
    return render(request, 'roompage.html')
