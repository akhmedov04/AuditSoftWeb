from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def home(request):
    data = {
        'blog': Maqola.objects.all()
    }
    return render(request, 'blog.html', data)