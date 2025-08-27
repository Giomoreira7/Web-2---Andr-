from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, TokenViewSet, UserTokenViewSet, TransactionViewSet, UserGamePlayViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'tokens', TokenViewSet)
router.register(r'usertokens', UserTokenViewSet)
router.register(r'transactions', TransactionViewSet)
router.register(r'usergameplays', UserGamePlayViewSet)

urlpatterns = router.urls