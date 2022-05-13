from django.shortcuts import render
from django.shortcuts import render
from .models import Blog

def home(request):
    return render(request, 'pages/home.html')
