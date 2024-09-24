from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AuteurViewSet, LivreAudioViewSet

router = DefaultRouter()
router.register(r'auteurs', AuteurViewSet, basename='auteurs')
router.register(r'livres_audio', LivreAudioViewSet, basename='livres_audio')

urlpatterns = [
    path('', include(router.urls)),
]
