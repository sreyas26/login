from django.shortcuts import render,redirect
from loginapp.models import Login
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def login(request):
    return render(request,'login.html')

def addus(request):
    if request.method=='POST':
        uname=request.POST['username']
        passw=request.POST['password']
        email=request.POST['u_email']
        std=Login(Username=uname,Password=passw,Emailid=email)
        std.save()
        
        subject="Username and password"
        message=f'your username is: {uname}\n your password is: {passw}'
        

        send_mail(subject,message,settings.EMAIL_HOST_USER,[email])
        return redirect('/')
        