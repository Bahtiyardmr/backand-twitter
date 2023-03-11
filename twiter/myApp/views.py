from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import *
from django.urls import reverse

# <-------------------------------- INDEX --------------------------------------------------->
def index(request):
    user=request.user
    pagatitle='Anasayfa'
    twets=Tweet.objects.all().order_by('-id')
    if request.method == 'POST':
        if request.FILES:
            text = request.POST['text']
            image = request.FILES['image']

            tweet = Tweet(user=request.user, text=text, image=image)
            tweet.save()
        else:
            text = request.POST['text']

            tweet = Tweet(user=request.user, text=text)
            tweet.save()
        
    context={
        'pagatitle':pagatitle,
        'twets': twets,
        'user': user,
    }
    return render(request,'index.html',context)

# <-------------------------------- FOLLOW --------------------------------------------------->
def Follow(request):
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
    twets = Tweet.objects.filter().order_by('-id')
    context={
        'pagatitle':pagatitle,
        'twets': twets,
    }
    return render(request,'profils/myprofile.html',context)
            
    # <-------------------------------- USERPROFILE --------------------------------------------------->
def userProfile(request):
    pagatitle='@userprofile'
    user=request.user

    context={
        'pagatitle':pagatitle,
        'user': user,
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
        
        else:
            hataMessage = 'kullanici adi veya Sifreniz yanlis!'
            return render(request, 'users/login.html', {'hataMessage': hataMessage})
        
    context={
        'pagatitle':pagatitle,
    }
    return render(request,'users/login.html',context)


    # <-------------------------------- REGISTER --------------------------------------------------->
def Register(request):
    pagatitle='Register'

    
    context={
        'pagatitle':pagatitle,
    }
    
    
    if request.method =="POST":
        name=request.POST['name']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
         user = User.objects.create_user(first_name=name,username=username, email=email,password=password)
         user.save()
         return render(request, 'users/login.html')
     
 
    return render(request,'users/register.html',context)

 # <-------------------------------- logout --------------------------------------------------->
def logoutUser(request):
    logout(request)
    return redirect('loguotKesfet')



 # <-------------------------------- likes --------------------------------------------------->
def begeni(request):
    user=request.user
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        post_obj = Tweet.objects.get(id=post_id)

        if user in post_obj.liked.all():
            post_obj.liked.remove(user)
        else:
            post_obj.liked.add(user)
    return redirect('index')



