from django.contrib import admin
from .models import *
from  django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['id','email','cpf', 'telefone']
    search_fields = ['email','cpf']
    ordering = ['email']


# Register your models here.
admin.site.register(CustomUser,CustomUserAdmin)