from django.shortcuts import render
from .models import User
import random
from django.core.mail import send_mail
from django.conf import settings

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
 
def signup(request):
    if request.method=="POST":
        try:
            User.objects.get(email=request.POST['email'])
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
                return render(request,'signup.html',{'msg':msg})

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
                
                if user.usertype=="buyer":
                    return render(request,'index.html')
                else:
                    return render(request,'seller-index.html')

            
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
    user=User.objects.get(email=request.session['email'])
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
                    return render(request,'change-password.html')

            else:
                msg="New password & confirm new password does not matched" 
            
                return render(request, 'change-password.html', {'msg': msg})
               

        else:
            msg="old password does not matched"
           
            return render(request, 'change-password.html', {'msg': msg})
                                

    else:
        return render(request,'change-password.html')
        
  
def forgot_password(request):
    print("1")
    if request.method=="POST":
        print("2")
        try:
            user=User.objects.get(email=request.POST['email'])
            otp=random.randint(1000,9999)
            context = {}
            address = request.POST.get('email')
            subject = "OTP For Forgot Password"
            message = "your otp For forgot password Is "+str(otp)

            if address and subject and message:
                try:
                    send_mail(subject, message, settings.EMAIL_HOST_USER, [address])
                    context['result'] = 'Email sent successfully'
                    request.session['email1']=request.POST['email']
                    request.session['otp']=otp
                except Exception as e:
                    context['result'] = f'Error sending email: {e}'
            else:
                context['result'] = 'All fields are required'
    
            return render(request, "otp.html", context)
        except Exception as e:
            print("3")
            print(e)
            msg='Email Not Registerd' 
            return render(request,'forgot-password.html',{'msg':msg})    
    else:   
        return render(request,'forgot-password.html')
    
def verify_otp(request):
    otp1=int(request.session['otp'])
    otp2=int(request.POST['otp'])

    if otp1==otp2:
        del request.session['otp']
        return render(request,'new-password.html',{'msg':'Please Set Your New Password'})
    else:
        return render(request,'otp.html',{'msg':'Invalid OTP'})

def new_password(request):
    if request.POST['new_password']==request.POST['cnew_password']:
        user=User.objects.get(email=request.session['email1'])
        user.password=request.POST['new_password']
        user.save()
        msg="password updated sucessfully"
        del request.session['email1']
        return render(request,'login.html',{'msg':msg})
    else:
        msg="New Password & confirm new password does not matched"
        return render(request,'new-password.html',{'msg':msg})