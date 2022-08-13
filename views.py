from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth


# Create your views here.

def index1(request):
    if request.method=='POST':
        user_name=request.POST['user_name']
        password=request.POST['password']

        user=auth.authenticate(user_name=user_name,password=password)
        if user is not None:
            auth.index1(request,user)
            return redirect("/")
        else:
            messages.info(request,'invalid credentials')
            return redirect('index1')
        
    else:
        return render(request,'index1.html')  
           

def index2(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        phone_number=request.POST['phone_number']
        user_name=request.POST['user_name']
        password=request.POST['password']
        confirm_password=request.POST['confirm_password']
        
        if password==confirm_password:
            if User.objects.filter(user_name=user_name).exists():
                messages.info(request,'Username Taken')
                return redirect('index2')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email Taken')
                return redirect('index2')
            else :
                user=User.objects.create_user(user_name=user_name,password=password,email=email,first_name=first_name,last_name=last_name).exists();   
                user.save();
                print('user created')
                return redirect('index1')
            
        else:
            print('password not matching')
            return redirect('/')

    else:
                    return render(request,'index2.html')
        
        
