from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from .models import *
from .serializers import *
from rest_framework.response import Response
from random import randint

class CustomUserView(ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

class TokenView(ModelViewSet):
    queryset = Token.objects.all()
    serializer_class = TokenSerializer

class AccountView(ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

class AccountTokenView(ModelViewSet):
    queryset = AccountToken.objects.all()
    serializer_class = AccountTokenSerializer

class BetsView(ModelViewSet):
    queryset = Bets.objects.all()
    serializer_class = BetsSerializer

class TransactionsView(ModelViewSet):
    queryset = Transactions.objects.all()
    serializer_class = TransactionsSerializer


class BetTryView(APIView):
    def get(self, request):
        #logic
        value1 = randint(0,4)
        value2 = randint(0,4)
        value3 = randint(0,4)

        return Response(status=200, data={
            'bet1': value1,
            'bet2': value2,
            'bet3': value3,
        })
