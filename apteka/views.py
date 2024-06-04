from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def home(request):
    data = {
        'blog': Maqola.objects.all()
    }
    return render(request, 'apteka.html', data)

# def main(request):
#     if request.user.is_authenticated:
#         data = {
#             "user": request.user
#         }
#         return render(request, 'aptekalogged.html', data)
#     return redirect('/apteka/')

