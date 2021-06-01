from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponse
#from django.contrib.auth.models import auth
from django.contrib.auth import authenticate,login,logout#for autentication,login,logout
from .models import UserDetails
from django.contrib.auth.models import User

# Create your views here.


def userlogin(request):
    print('tys')
    if request.method == "POST":
        print('son')

        username = request.POST['username']
        password = request.POST['password']
        print(username,password)
        user = authenticate(request,username = username,password = password)

        if user is not None:
            login(request,user)
            return render(request,"home.html")
        else:
            messages.info(request,'Invalid Username and Password')
            return redirect('login')
    else:
        return render(request,'login.html')



def register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        phone_no = request.POST['phoneno']
        location = request.POST['location']

        #print(username,email,password1)
        
        if password1 == password2:
            if User.objects.filter(username = username).exists():
                messages.info(request,'Username already Exists')
                return redirect('register')
            elif User.objects.filter(email = email).exists():
                messages.info(request,'Email Already Exists')
                return redirect('register')
            else:
                usr = User.objects.create_user(username = username,email = email,password = password1)
                user_details = UserDetails(user = usr,phoneno = phone_no,location = location)
                usr.save()
                user_details.save()
                print('User Created')
                return redirect('login')
        else:
            messages.info(request,"Password is not matching")
            return redirect('register')
    else:
        return render(request,'register.html')

def home(request):
    return render(request,'home.html')

def logout(request):
    print("lir")
    #logout(request)
    return redirect('/')