from django.shortcuts import render
from .models import User

# Create your views here.
def index(request):
    return render(request,'index.html')

def shop(request):
    return render(request,'shop.html')

def about(request):
    return render(request,'about.html')

def services(request):
    return render(request,'services.html')

def blog(request):
    return render(request,'blog.html')

def contact(request):
    return render(request,'contact.html')

def login(request):
    return render(request,'login.html')

def signup(request):
    if request.method=="POST":
        try:
            user=User.objects.get(email=request.POST['email'])
            msg="Email Already Registerd"
            return render(request,'login.html',{'msg':msg})
        except:
            if request.POST['password'] == request.POST['cpassword']:
                User.objects.create(
                    fname=request.POST['fname'],
                    lname=request.POST['lname'],
                    email=request.POST['email'],
                    mobile=request.POST['mobile'],
                    address=request.POST['address'],
                    password=request.POST['password'],
                    profile_picture=request.FILES['profile_picture'],
                    usertype=request.POST['usertype']
                )
                msg="user sign up successfully"
                return render(request,'login.html',{'msg':msg})
            else:
                msg="password & confirm password does not matched"
                return render(request,'login.html',{'msg':msg})

    else:
        return render(request, 'signup.html') 