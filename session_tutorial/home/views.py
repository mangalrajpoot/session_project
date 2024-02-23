from django.shortcuts import render,redirect
from .models import User_Register
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    if request.method == 'GET':
        return render(request,'home/index.html')
    else:
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        request.session['user']=request.POST['username']
        r=User_Register(username=username,email=email,password=password)
        r.save()
        return render(request,'home/login.html',{'msg':'User Account Created Successfully !','user':request.session['user']})
    
def login(request):
    if request.method == 'GET':
        return render(request,'home/login.html')
    else:
        username=request.POST['username']
        password=request.POST['password']
        
        r=User_Register.objects.filter(username=username,password=password)
        if r:
            return redirect('profile')
        else:
            return render(request,'home/login.html',{'msg':'Invalid Username or Password!'})
        

def profile(request):
    user = request.session.get('user')  # Use get() method to avoid KeyError
    if user is None:
        return redirect('login')
    else:
        return render(request, 'home/profile.html', {'user': user})

        
