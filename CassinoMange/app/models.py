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
    data_criacao = models.DateField()
    data_insercao = models.DateField(auto_now_add=True)
    codigo = models.CharField(max_length=10, unique=True)
    descricao = models.TextField()
    valor_em_mangecoin = models.DecimalField(max_digits=20, decimal_places=8)

    def __str__(self):
        return f"{self.nome} ({self.codigo})"


class UserToken(models.Model):
    user_email = models.CharField(max_length=255)  # Armazena o email do usuário manualmente
    token_codigo = models.CharField(max_length=10)  # Armazena o código do token manualmente
    quantidade = models.DecimalField(max_digits=20, decimal_places=8, default=0)

    def __str__(self):
        return f"{self.user_email} - {self.token_codigo}: {self.quantidade}"


class Transaction(models.Model):
    user_email = models.CharField(max_length=255)     # Armazena o email do usuário
    token_codigo = models.CharField(max_length=10)   # Armazena o código do token
    quantidade = models.DecimalField(max_digits=20, decimal_places=8)
    data_transacao = models.DateTimeField(auto_now_add=True)
    tipo = models.CharField(max_length=10, choices=(('compra', 'Compra'), ('venda', 'Venda')))

    def __str__(self):
        return f"{self.tipo} - {self.user_email} - {self.token_codigo } - {self.quantidade}"



class UserGamePlay(models.Model):
    user_email = models.EmailField(max_length=255)
    jogo = models.CharField(max_length=100)
    pontuacao = models.IntegerField()
    data_jogo = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user_email} - {self.jogo} - {self.pontuacao}"