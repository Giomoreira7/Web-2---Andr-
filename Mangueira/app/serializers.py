from .models import *
from rest_framework import serializers

class CustomUserseralizer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'
        many = True