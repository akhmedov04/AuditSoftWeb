from django.shortcuts import render, redirect

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        return redirect('/main/')
    return render(request, 'index.html')

def main(request):
    if request.user.is_authenticated:
        data = {
            "user": request.user
        }
        return render(request, 'main.html', data)
    return redirect('/')

def profil(request):
    if request.user.is_authenticated:
        data = {
            "user":request.user
        }
        return render(request, 'profile.html', data)
    return redirect('/')