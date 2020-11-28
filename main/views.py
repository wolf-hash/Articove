from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import login, logout, authenticate
from .models import *
# from accounts.models import UserAccount


def index(request):
    if request.user.is_anonymous:
        return render(request, 'index/index.html', {'form_action': 'login', 'button_name': 'Login'})
    else:
        return render(request, 'index/index.html', {'form_action': 'logout', 'button_name': 'Logout'})

def gallery(request):
    return render(request, "index/gallery.html")

def Login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(email=email, password=password)
        login(request, user=user)
        return redirect("/")
        
    return render(request, 'index/login.html')

def Logout(request):
    logout(request)
    return redirect('/')
