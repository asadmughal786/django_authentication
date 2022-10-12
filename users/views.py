
from django.contrib import messages
from django.shortcuts import render,redirect
from .models import User_signup
# from django.contrib.auth.models import User
# Create your views here.

def index(request):
    return render(request,"users/base.html")
def sign_up(request):
    if request.method == "POST":
        First_name = request.POST.get('firstName'),
        Last_name = request.POST.get('lastName')
        Contact_number = request.POST.get('contactNumber')
        CNIC = request.POST.get('cnic')
        Pass_word = request.POST.get('password')
        Conf_passsword = request.POST.get('confPassword')
        User_email = request.POST.get('email')
        User_address = request.POST.get('Address')
        print(f'First Name: {str(list(First_name)[0])},Last Name: {Last_name},CNIC: {CNIC}, Email: {User_email}')
        user_data = User_signup.objects.filter(user_email = User_email)
        if user_data:
            messages.info(request,"Email Already Exsists")
            return redirect('signup')
        if Pass_word == Conf_passsword:
            user_data = User_signup(user_fname = str(list(First_name)[0]) , user_lname = Last_name, user_contact = Contact_number, user_cnic = CNIC ,user_email= User_email,user_address = User_address, user_password= Pass_word,user_conf_password=Conf_passsword)
            # user_data.set_password(Pass_word)
            user_data.save()
            messages.info(request,"User saved successfully")        
            return redirect("signup")
        else:
            messages.warning(request,'Passwords does not match')
            return redirect("signup")
    return render(request,'users/signup.html')

def login(request):
    if request.method == "POST":
        login_email = request.POST.get('login_email')
        login_password = request.POST.get('login_password')
        print(f'{login_email}, {login_password}')
        user = User_signup.objects.filter(user_email = login_email, user_password = login_password).first()

        if user:
            messages.info(request,f'Welcome {user.user_fname} to the login',)
            return redirect('login')
        else:
            messages.info(request,'Invalid Email or Password')


    return render(request,'users/login.html')