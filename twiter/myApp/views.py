from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from .models import *

# <-------------------------------- INDEX --------------------------------------------------->
def index(request):
    pagatitle='Anasayfa'

    context={
        'pagatitle':pagatitle,
    }
    return render(request,'index.html',context)

# <-------------------------------- FOLLOW --------------------------------------------------->
def Folow(request):
    pagatitle='Takip edilenler'

    context={
        'pagatitle':pagatitle,
    }
    return render(request,'takip.html',context)

    # <-------------------------------- KESFET --------------------------------------------------->
def Kesfet(request):
    pagatitle='Kesfet'

    context={
        'pagatitle':pagatitle,
    }
    return render(request,'kesfet.html',context)

            
    # <-------------------------------- MYPROFILE --------------------------------------------------->
def myProfil(request):
    pagatitle='Profilim'

    context={
        'pagatitle':pagatitle,
    }
    return render(request,'profils/myprofile.html',context)
            
    # <-------------------------------- USERPROFILE --------------------------------------------------->
def userProfile(request):
    pagatitle='@userprofile'

    context={
        'pagatitle':pagatitle,
    }
    return render(request,'profils/userprofil.html',context)
            
    # <-------------------------------- LOGUOTKESFET --------------------------------------------------->
def loguotKesfet(request):
    pagatitle='Kesfet/Twitter'

    context={
        'pagatitle':pagatitle,
    }
    return render(request,'loguotkesfet.html',context)


    # <-------------------------------- LOGIN --------------------------------------------------->
def Login(request):
    pagatitle='Kesfet/Twitter'

    if request.method =='POST':
        username=request.POST['username']
        password=request.POST['password']
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('index')
    context={
        'pagatitle':pagatitle,
    }
    return render(request,'users/login.html',context)


    # <-------------------------------- REGISTER --------------------------------------------------->
def Register(request):
    pagatitle='Kesfet/Twitter'

    context={
        'pagatitle':pagatitle,
    }
    return render(request,'users/register.html',context)