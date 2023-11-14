
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import RegisterForm

from .models import Register, Registration


def index(request):
    return render(request,'index.html')
def blank(request):
    return render(request,'blank.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        users = Register.objects.filter(username=username,password=password ).exists()
        print(users)
        if users is not False:
            return redirect('/blank')
        else:
            print("invalid")
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        if password==confirm_password:
            reg=Register(username=username,password=password,confirm_password=confirm_password)
            reg.save()
            return redirect('/login')
        else:
            print("password not match")
    return render(request,'register.html')


def newpage(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.info(request,"Application Accepted")

        else:
            print("invalid")
    return render(request, 'newpage.html')


def logout(request):
    logout(request)
    return redirect('/login')


