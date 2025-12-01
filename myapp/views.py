from django.shortcuts import render
from .models import User

# Create your views here.
def index(request):
    return render(request,'index.html')

def contact(request):
    return render(request,'contact.html')

def category(request):
    return render(request,'category.html')

 

def signup(request):
    if request.method=="POST":
         try:
             User.objects.get(email=request.POST['email'])
             msg="Email Already Registered"
             return render(request,'signup.html',{'msg':msg})
         except User.DoesNotExist:
             if request.POST['password']==request.POST['cpassword']:
                 User.objects.create(
                     fname=request.POST['fname'],
                     lname=request.POST['lname'],
                     email=request.POST['email'],
                     mobile=request.POST['mobile'],
                     address=request.POST['address'],
                     password=request.POST['password'],
                     profile_picture=request.FILES.get('profile_picture')
                 )
                 msg="User Signup Successful"
                 return render(request,'signup.html',{'msg':msg})
             else:
                 msg="Pass & Cpass Doesnt Match"
                 return render(request,'signup.html',{'msg':msg})
    else:
        return render(request,'signup.html')
    

def login(request):
    return render(request,'login.html')