from django.urls import path, include
from rest_framework.routers import DefaultRouter
from.views import AbonnementViewSet, TransactionViewSet

router = DefaultRouter()
router.register(r'abonnements', AbonnementViewSet, basename='abonnements')
router.register(r'transactions', TransactionViewSet, basename='transactions')

urlpatterns = [
    path("", include(router.urls)),
]
