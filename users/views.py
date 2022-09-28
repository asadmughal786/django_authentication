import email
from email import message
from django.contrib import messages
from pyexpat.errors import messages
from django.shortcuts import render,redirect
from .models import User_signup
# from django.contrib.auth.models import User

# Create your views here.
def index(request):
    return render(request,"users/base.html")
def log_in(request):
    if request.method == "POST":
        First_name = request.POST.get('firstName'),
        Last_name = request.POST.get('lastName')
        Contact_number = request.POST.get('contactNumber')
        CNIC = request.POST.get('cnic')
        Pass_word = request.POST.get('password')
        Conf_passsword = request.POST.get('confPassword')
        User_email = request.POST.get('email')
        User_address = request.POST.get('Address')
        print(f'First Name: {list(First_name)[0]},Last Name: {Last_name},CNIC: {CNIC}, Email: {User_email}')
        user_data = User_signup.objects.filter(user_email = User_email)
        if user_data:
            messages.info(request,"Email Already Exsists")
            return redirect('log_in')
        if Pass_word == Conf_passsword:
            user_data = User_signup(user_fname = First_name , user_lname = Last_name, user_contact = Contact_number, user_cnic = CNIC ,user_email= User_email,user_address = User_address, user_password= Pass_word,user_conf_password=Conf_passsword)
            # user_data.set_password(Pass_word)
            user_data.save()
            messages.info(request,"User saved successfully")        
            return redirect("log_in")
        else:
            messages.warning(request,'Passwords does not match')
            return redirect("log_in")
    return render(request,'users/login.html')


    #return render(request,"users/login.html")

def action_signup(request):
    pass