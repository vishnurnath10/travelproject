from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method == 'POST':
        login_username = request.POST['user_name']
        login_password = request.POST['password']
        login_user = auth.authenticate(username=login_username,password=login_password)


        if login_user is not None:
            auth.login(request,login_user)
            return redirect('/')
        else:
            messages.info(request,'invalid details')
            return redirect('login')

    return render(request,'login.html')
def register(request):
    if request.method == 'POST':
        username = request.POST['user_name']
        firstname = request.POST['first_name']
        lastname = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['confirm_password']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email taken")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, first_name=firstname, last_name=lastname,email=email,password=password)
                user.save();
                return redirect('login')
        else:
            messages.info(request,'password not matching')
            return redirect('regiser')
        return redirect('/')

    return render(request,'register.html')
def logout(request):
    auth.logout(request)
    return redirect('/')