from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"users/base.html")
def log_in(request):
    return render(request,"users/login.html")

def action_signup(request):
    pass