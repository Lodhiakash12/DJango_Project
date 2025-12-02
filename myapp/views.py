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
            user=User.objects.get(email=request.POST['email'])
            msg="Email Already Registerd"
            return render(request,'login.html',{'msg':msg})
        except:
            if request.POST['password']==request.POST['cpassword']:
                User.objects.create(
                    fname=request.POST['fname'],
                    lname=request.POST['lname'],
                    email=request.POST['email'],
                    mobile=request.POST['mobile'],
                    address=request.POST['address'],
                    password=request.POST['password'],
                    profile_picture=request.FILES['profile_picture'],
                )
                msg="user sign up successfully"
                return render(request,'login.html',{'msg':msg})
            else:
                msg="password & confirm password does not matched"
                return render(request,'login.html',{'msg':msg})

    else:
        return render(request, 'signup.html') 
    

def login(request):
    if request.method=="POST":
        try:
            user=User.objects.get(email=request.POST['email'])
            if user.password==request.POST['password']:
                request.session['email']=user.email
                request.session['fname']=user.fname
                request.session['profile_picture']=user.profile_picture.url
                return render(request,'index.html')
            else:
                msg="Incorrect password" 
                return render(request,'login.html',{'msg':msg}) 

        except:
               msg="Email Not Registerd" 
               return render(request,'login.html',{'msg':msg})      

        
    else:
        return render(request, 'login.html')   
    
def logout(request):
    try:
        del request.session['email']       
        del request.session['fname']    
        del request.session['profile_picture'] 
        msg="Logged out succesfully"
        return render(request,'login.html',{'msg':msg})    
    except:
         msg="Logged out succesfully"
         return render(request,'login.html',{'msg':msg})   
    
def profile(request):
    user=User.objects.get(email=request.session['email'])
    if request.method=='POST':
        user.fname=request.POST['fname']
        user.lname=request.POST['lname']
        user.mobile=request.POST['mobile']
        user.address=request.POST['address']
        try:
            user.profile_picture=request.FILES['profile_picture']
        except:
            pass
        user.save()
        request.session['profile_picture']=user.profile_picture.url
        msg="profile updated successfully"        
        return render(request,'profile.html',{'user':user,'msg':msg}) 

    else:
        return render(request,'profile.html',{'user':user}) 
    
def change_password(request):
    if request.method=='POST':
        user=User.objects.get(email=request.session['email'])
        if user.password==request.POST['old_password']:
            if request.POST['new_password']==request.POST['cnew_password']:
                if user.password!=request.POST['new_password']:
                      user.password=request.POST['new_password']
                      user.save()
                      del request.session['email']       
                      del request.session['fname']    
                      del request.session['profile_picture'] 
                      msg="password change succesfully"
                      return render(request,'login.html',{'msg':msg})  
                else:
                    msg="your new password cant be from your old password"
                    return render(request, 'change-password.html', {'msg': msg})

            else:
                msg="New password & confirm new password does not matched" 
                return render(request,'change-password.html',{'msg':msg}) 

        else:
            msg="old password does not matched"
            return render(request,'change-password.html',{'msg':msg})                     

    else:
        return render(request,'change-password.html')


