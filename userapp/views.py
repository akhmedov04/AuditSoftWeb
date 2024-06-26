from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import *
from django.contrib import messages



# def registerview(request):
#     if request.method == "POST" and request.POST.get('p') == request.POST.get('cp'):
#         username = request.POST.get('l')
#         if User.objects.filter(username=username).exists():
#             messages.error(request, 'Username is already taken')
#         else:
#             User.objects.create_user(
#                 username=username,
#                 password=request.POST.get('p')
#             )
#             return redirect('/user/login/')
#     return render(request, 'register.html')


def loginview(request):
    if request.user.is_authenticated:
        return redirect('/main/')
    else:
        if request.method == 'POST':
            username = request.POST['l']
            password = request.POST['p']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/main/')
            else:
                messages.error(request, 'Invalid username or password')
        return render(request, 'login.html')

def logoutview(request):
    logout(request)
    return redirect('/')