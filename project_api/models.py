from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""

    def create_user(self, email, name, password=None):
        """Create a new user profile"""
        if not email:
            raise ValueError('User must have an email adress')

        email = self.normalize_email(email) #TODO what is normalize_email????
        user = self.model(email=email, name=name)

        # we wanna make sure the password sure be encrypted by using set_password:
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self,email, name, password):
        """Create and save a new superuser with given details"""
        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for user in the system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """"Retrive full name of user"""
        return self.name

    def get_short_name(self):
        """Retrive short name of user"""
        return self.name

    def __str__(self):
        """Return string representation of our user"""
        return self.email


class Cliente(models.Model):
    """Modelo que representa o terceiro"""
    nome = models.CharField(max_length=200)
    data_de_cadastro = models.DateTimeField(auto_now_add=True)
    #TODO: add field excluido in the future
    ultima_alteracao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ['nome']


class Produto(models.Model):
    """Model que representa os produtos"""
    nome = models.CharField(max_length=200)
    codigo = models.CharField(max_length=120)
    tabela_preco = models.DecimalField(max_digits=20, decimal_places=2, verbose_name='Preço Unitário')
    multiplo = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    #TODO: Do not accept negative numbers in the fields tabela_preco and multiplo
    data_cadastro=models.DateTimeField(auto_now=True)
    ultima_alteracao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ['nome']


class Pedido(models.Model):
    """Model que representa os pedidos"""
    cliente = models.ForeignKey('Cliente', on_delete=models.SET_NULL, null=True)
    #TODO: Maybe add the field number in the future
    total = models.DecimalField(max_digits=20, decimal_places=2)
    #TODO: Do not accept negative numbers in the field total
    data_criacao = models.DateTimeField(auto_now=True)
    data_emissao = models.DateField(auto_now=True)
    info_adicionais = models.CharField(max_length=500, blank=True, null=True, verbose_name='Informaçõs Adicionais')
    condicao_pagamento = models.CharField(max_length=120)
    ultima_alteracao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.razao_social

class ItemPedido(models.Model):
    produto = models.ForeignKey('Produto', on_delete=models.SET_NULL, null=True)
    pedido = models.ForeignKey('Pedido', on_delete=models.SET_NULL, null=True, related_name='itens')
    quantidade = models.DecimalField(max_digits=20, decimal_places=2)
    total_item = models.DecimalField(max_digits=20, decimal_places=2)
    preco_tabela = models.DecimalField(max_digits=20, decimal_places=2)
    preco_liquido = models.DecimalField(max_digits=20, decimal_places=2)
    ultima_alteracao = models.DateTimeField(auto_now=True)
