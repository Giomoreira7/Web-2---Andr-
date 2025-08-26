
from django.shortcuts import render
from rest_framework import viewsets
from .models import CustomUser, Token, UserToken, Transaction, UserGamePlay
from .serializers import UserSerializer, TokenSerializer, UserTokenSerializer, TransactionSerializer, UserGamePlaySerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

class TokenViewSet(viewsets.ModelViewSet):
    queryset = Token.objects.all()
    serializer_class = TokenSerializer

class UserTokenViewSet(viewsets.ModelViewSet):
    queryset = UserToken.objects.all()
    serializer_class = UserTokenSerializer

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

class UserGamePlayViewSet(viewsets.ModelViewSet):
    queryset = UserGamePlay.objects.all()
    serializer_class = UserGamePlaySerializer
