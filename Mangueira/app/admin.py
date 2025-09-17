from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin

class AdminCustomUser(UserAdmin):
    model = CustomUser
    list_display = [ 'email', 'cpf']
    list_display_links = ( 'email',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions',{'fields': ('is_active','is_staff','is_superuser')}),
        ('Monitoring', {'fields': ('last_login',)}),
        ('User data', {'fields': ('name', 'cpf', 'rg',)}),
        ('Address', {'fields': ('address_street', 'address_district', 'address_number',
                       'address_zip_code', 'address_city', 'address_state', 
                       'address_country',)}),        

    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'cpf', 'rg', 'address_street', 'address_district', 'address_number',
                       'address_zip_code', 'address_city', 'address_state', 
                       'address_country'),
        }),
    )
    
                       
    ordering = ['email']

admin.site.register(CustomUser, AdminCustomUser)
