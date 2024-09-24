from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AvisViewSet

router = DefaultRouter()
router.register(r'avis', AvisViewSet, basename='avis')

urlpatterns = [
    path('', include(router.urls)),
]
