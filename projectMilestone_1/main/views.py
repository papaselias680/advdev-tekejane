from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def home(request):
    return render(request, 'main/home.html', {'title': 'Home'})

def about(request):
    return render(request, 'main/about.html', {'title': 'About'})   