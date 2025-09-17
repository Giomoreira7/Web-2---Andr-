from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .custom_user_maneger import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    cpf = models.CharField(max_length=14, unique=True)
    rg = models.CharField(max_length=20)
    address_street = models.CharField(max_length=400)
    address_district = models.CharField(max_length=400)
    address_number = models.CharField(max_length=10)
    address_zip_code = models.CharField(max_length=15)
    address_city = models.CharField(max_length=400)
    address_state = models.CharField(max_length=400)
    address_country = models.CharField(max_length=400)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'cpf', 'rg', 'address_street', 'address_district',
                       'address_number', 'address_zip_code', 'address_city',
                       'address_state', 'address_country']

    objects = CustomUserManager()

    def __str__(self):
        return self.email


CATEGORIAS = [
    ('Escritorio', 'Escritório'),
    ('Jantar', 'Jantar'),
    ('Sala de Estar', 'Sala de Estar'),
    ('Infantil', 'Infantil'),
]

PAGAMENTO = [
    ('Pix', 'Pix'),
    ('Boleto', 'Boleto'),
    ('Cartao', 'Cartão de Crédito'),
]

STATUS_PEDIDO = [
    ('EM PROCESSAMENTO', 'EM PROCESSAMENTO'),
    ('PAGAMENTO APROVADO', 'PAGAMENTO APROVADO'),
    ('NOTA FISCAL EMITIDA', 'NOTA FISCAL EMITIDA'),
    ('EM PREPARAÇÃO', 'EM PREPARAÇÃO'),
    ('ENVIADO', 'ENVIADO'),
    ('RECEBIDO', 'RECEBIDO'),
    ('PAGAMENTO REPROVADO', 'PAGAMENTO REPROVADO'),
    ('CANCELADO', 'CANCELADO'),
    ('SOLICITAÇÃO DE DEVOLUÇÃO', 'SOLICITAÇÃO DE DEVOLUÇÃO'),
    ('EM DEVOLUÇÃO', 'EM DEVOLUÇÃO'),
    ('DEVOLVIDO', 'DEVOLVIDO'),
    ('DEVOLUÇÃO CANCELADA', 'DEVOLUÇÃO CANCELADA'),
]



class Produtos(models.Model):
    imagem = models.TextField()
    name = models.CharField(max_length=255, unique=True)
    avaliacao = models.DecimalField(max_digits=2, decimal_places=1, default=0.0)
    quant_av = models.IntegerField(default=0)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    parcelamento = models.CharField(max_length=50)
    categoria = models.CharField(max_length=50, choices=CATEGORIAS)

    def __str__(self):
        return f"{self.name} ({self.categoria})"



class Conjunto(models.Model):
    produto = models.ForeignKey(Produtos, related_name='conjuntos', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    medidas = models.CharField(max_length=100)
    peso = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.name} ({self.produto.name})"



class Pedido(models.Model):
    usuario = models.ForeignKey(CustomUser, related_name='pedidos', on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    desconto = models.DecimalField(max_digits=10, decimal_places=2)
    pagamento = models.CharField(max_length=20, choices=PAGAMENTO)
    status = models.CharField(max_length=50, choices=STATUS_PEDIDO)
    codigo_rastreamento = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"Pedido #{self.id} - {self.usuario.email}"



class Carrinho(models.Model):
    pedido = models.ForeignKey(Pedido, related_name='carrinho', on_delete=models.CASCADE)
    produto = models.ForeignKey(Produtos, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.quantidade}x {self.produto.name}"



class Cartao(models.Model):
    pedido = models.ForeignKey(Pedido, related_name='cartao', on_delete=models.CASCADE)
    numero = models.CharField(max_length=16)
    validade = models.DateField()
    nome = models.CharField(max_length=200)
    codigo = models.CharField(max_length=4)

    def __str__(self):
        return f"Cartão de {self.nome}"

class Devolucao(models.Model):
    pedido = models.ForeignKey(Pedido, related_name='devolucoes', on_delete=models.CASCADE)
    item = models.ForeignKey(Carrinho, on_delete=models.CASCADE)
    motivo = models.CharField(max_length=1000)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
      return (
    f"Devolução do pedido {self.pedido.id} "
    f"{self.item.produto.name}"
)