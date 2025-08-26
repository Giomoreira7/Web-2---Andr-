from django.contrib.auth.models import BaseUserManager

class CustomUserManager(BaseUserManager):

    def create_user(self, email, password=None, cpf=None, rg=None, data_nascimento=None, rua=None, telefone=None, foto=None, **extra_fields):
        if None in (email, password, cpf, rg, data_nascimento, rua, telefone):
            raise ValueError("Campos obrigatórios não informados!")
        email_normalized = self.normalize_email(email)
        extra_fields.setdefault("is_active", True)
        user = self.model(
            email=email_normalized,
            cpf=cpf,
            rg=rg,
            data_nascimento=data_nascimento,
            rua=rua,
            telefone=telefone,
            foto=foto,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, cpf=None, rg=None, data_nascimento=None, rua=None, telefone=None, foto=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(email, password, cpf, rg, data_nascimento, rua, telefone, foto, **extra_fields)
