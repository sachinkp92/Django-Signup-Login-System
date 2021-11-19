from django.shortcuts import render,HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


def signup(request):
    if request.method =="POST":
        uname=request.POST['username']
        uemail = request.POST['email']
        upassword = request.POST['password']
        x=User.objects.create_user(username=uname, email=uemail, password=upassword)
        x.save()
        return HttpResponse("<h1> User Signup Successfully<h1>")
    else:
        return render(request,'signup.html')

def user_login(request):
    if request.method =="POST":
        uname=request.POST['username']
        upassword = request.POST['password']
        user=authenticate(request,username =uname, password =upassword)
        if user is not None:
            login(request,user)
            return redirect('dashboard')
        else:
            return redirect('login')
    else:
        return render(request, 'login.html')

def dashboard(request):
    if request.user.is_authenticated:
        return render(request, 'dashboard.html')
    else:
        return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return redirect('login')




