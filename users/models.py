from statistics import mode
from django.db import models

# from django import forms
# Create your models here.


class User_signup(models.Model):
    user_fname = models.TextField(max_length=20, null=False)
    user_lname = models.TextField(max_length=20, null=False)
    user_email = models.EmailField(null=False)
    user_contact = models.IntegerField(null=False)
    user_cnic = models.IntegerField(null=False)
    user_address = models.TextField(max_length=255,null=True,blank=True)
    user_password = models.CharField(max_length=8)
    user_conf_password = models.CharField(max_length=8)