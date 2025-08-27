from django.db import models
from .user_maneger import CustomUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

class CustomUser(AbstractBaseUser, PermissionsMixin):
    name= models.CharField(("Nome"),max_length=255)
    email = models.EmailField(("email"), unique=True)
    cpf = models.CharField(("CPF"), max_length=12, unique=True)
    rg = models.CharField(("RG"), max_length=12, unique=True)
    birth_date= models.DateField(("Data de nascimento"))
    address_street = models.TextField(("Rua"),max_length=400)
    address_number =models.CharField (("numero"), max_length=10)
    address_district = models.TextField(("bairro"))
    address_zip_code = models.CharField(("CEP"), max_length=20)
    address_city = models.CharField(("Cidade"))
    address_state = models.CharField(("Estado"))
    address_country =models.TextField(("País"))
    phone = models.CharField(("Telefone"), max_length=20)
    photo = models.TextField(("Foto (URL)"), blank=True, null=True)
    
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name','cpf', 'rg', 'birth_date', 'address_street','address_number','address_district','address_zip_code','address_city','address_state','address_country','phone']

    def __str__(self):
        return self.email


class Token(models.Model):
    name= models.CharField(("Nome"),max_length=255)    
    date_creation = models.DateField()
    date_insertion = models.DateField(auto_now_add=True)
    code = models.CharField(max_length=10, unique=True)
    description = models.TextField( blank=True, null=True)
    conversion = models.DecimalField(max_digits=20, decimal_places=4)


    def __str__(self):
        return self.code

    
class Account(models.Model):
   user_FK = models.ForeignKey(CustomUser, related_name='Account_user_FK', on_delete=models.CASCADE)    
   date_open = models.DateField(auto_now_add=True)
   date_close = models.DateField (null=True, blank=True)

   def __str__(self):
        return self.user_FK.email

class UserToken(models.Model):
    Account_FK = models.ForeignKey(Account, related_name='UserToken_account_FK', on_delete=models.CASCADE)
    Token_FK = models.ForeignKey  (Token, related_name='UserToken_token_FK', on_delete=models.CASCADE)
    quantidade = models.DecimalField(max_digits=20, decimal_places=4, default=0)

    def __str__(self):
        return f"{self.Account_FK} - {self.Token_FK}"


class Transaction(models.Model):
    Account_FK = models.ForeignKey(Account, related_name='Transactions_account_FK', on_delete=models.CASCADE)        
    quantidade_FK = models.DecimalField(max_digits=20, decimal_places=8)
    date_transaction = models.DateTimeField(auto_now_add=True)
    oken_source_FK = models.ForeignKey(Token, related_name='Transactions_token_source_FK', on_delete=models.CASCADE)    
    token_target_FK = models.ForeignKey(Token, related_name='Transactions_token_target_FK', on_delete=models.CASCADE)
    token_source_amount = models.DecimalField(max_digits=12, decimal_places=4)
    token_target_amount = models.DecimalField(max_digits=12, decimal_places=4)

    def __str__(self):
        return f'{self.token_source_FK.name}-{self.token_target_FK.name}'



class UserGamePlay(models.Model):
    Account_FK = models.ForeignKey(Account, related_name='UserGamePlay_account_FK', on_delete=models.CASCADE)        
    is_loss = models.BooleanField(default=False)
    input_amount = models.DecimalField(max_digits=12, decimal_places=4)
    output_amount = models.DecimalField(max_digits=12, decimal_places=4)
    value1 = models.IntegerField()
    value2 = models.IntegerField()
    value3 = models.IntegerField()
    
    def __str__(self):
        return f'{self.account_FK.id}'