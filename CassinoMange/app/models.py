from django.db import models
from .user_maneger import CustomUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(("email"), unique=True)
    cpf = models.CharField(("CPF"), max_length=14, unique=True)
    rg = models.CharField(("RG"), max_length=20, unique=True)
    data_nascimento = models.DateField(("Data de nascimento"))
    rua = models.TextField(("Rua"))
    bairro = models.TextField(("bairro"))
    cep = models.CharField(("CEP"), max_length=20)
    telefone = models.CharField(("Telefone"), max_length=20)
    foto = models.URLField(("Foto (URL)"), blank=True, null=True)
    
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['cpf', 'rg', 'data_nascimento', 'rua','bairro','cep','telefone']

    def __str__(self):
        return self.email


class Token(models.Model):
    nome = models.CharField(max_length=100)
    simbolo = models.CharField(max_length=10)
    valor = models.DecimalField(max_digits=20, decimal_places=8)  # exemplo para valor token
    
    def __str__(self):
        return f"{self.nome} ({self.simbolo})"


class UserToken(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    token = models.ForeignKey(Token, on_delete=models.CASCADE)
    quantidade = models.DecimalField(max_digits=20, decimal_places=8, default=0)
    
    def __str__(self):
        return f"{self.user.email} - {self.token.simbolo}: {self.quantidade}"


class Transaction(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    token = models.ForeignKey(Token, on_delete=models.CASCADE)
    quantidade = models.DecimalField(max_digits=20, decimal_places=8)
    data_transacao = models.DateTimeField(auto_now_add=True)
    tipo = models.CharField(max_length=10, choices=(('compra', 'Compra'), ('venda', 'Venda')))
    
    def __str__(self):
        return f"{self.tipo} - {self.user.email} - {self.token.simbolo} - {self.quantidade}"


class UserGamePlay(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    jogo = models.CharField(max_length=100)
    pontuacao = models.IntegerField()
    data_jogo = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.email} - {self.jogo} - {self.pontuacao}"
