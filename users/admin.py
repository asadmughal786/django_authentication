from django.contrib import admin
from .models import User_signup

# Register your models here.

@admin.register(User_signup)
class Users(admin.ModelAdmin):
    list_display = ['id','user_fname','user_lname','user_cnic', 'user_email','user_contact', 'user_address','user_password','user_conf_password']
    list_display_links = ['id', 'user_email', 'user_contact']
    readonly_fields = ('user_email','user_contact')
