from django.shortcuts import render, redirect
from .models import Profil
from django.contrib.auth import authenticate, login
# Create your views here.

def profiles(request):
    users = Profil.objects.all()
    context = {
        'users': users
    }

    return render(request, 'main.html', context)

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request,username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profiles')
        else:
            print('Bunday login va parol mavjud emas!')