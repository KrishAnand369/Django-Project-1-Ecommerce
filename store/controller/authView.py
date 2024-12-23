from django.contrib import messages
from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from store.form import CustomUserForm
from django.contrib.auth import authenticate,login,logout

def register(request):
    form = CustomUserForm()
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Registered Successfuly! Login to Continue')
            return redirect('/login')
        else:
            print(form.errors)
    context = {'form':form}

    return render(request,'store/auth/register.html',context)

def loginpage(request):
    if request.user.is_authenticated:
        messages.warning(request,"You are already registered,Can Login Now")
        return redirect('/')
    else:
        if request.method == 'POST':
            name=request.POST.get('username')
            password=request.POST.get('password')
            user = authenticate(request,username=name,password =password)

            if user is not None:
                login(request,user)
                messages.success(request,"Logged in Successfully")
                return redirect('/')
            else:
                messages.error(request,"Invalid username or password")
                return redirect('/login')
    return render(request,'store/auth/login.html')

def logoutpage(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request,"Logged Out Successfully")
    return redirect('/')

