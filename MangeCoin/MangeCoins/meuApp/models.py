from django.db import models
from .user_maneger import CustomUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(("email"), unique=True)
    cpf = models.CharField(("CPF"), max_length=14, unique=True)
    rg = models.CharField(("RG"), max_length=20, unique=True)
    data_nascimento = models.DateField(("Data de nascimento"))
    endereco_completo = models.TextField(("Endereço completo"))
    telefone = models.CharField(("Telefone"), max_length=20)
    foto = models.URLField(("Foto (URL)"), blank=True, null=True)  # foto opcional (link externo)
    
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['cpf', 'rg', 'data_nascimento', 'endereco_completo', 'telefone']

    def __str__(self):
        return self.email