from rest_framework import viewsets
from .models import Auteur, LivreAudio
from .serializer import AuteurSerializer, LivreAudioListSerializer, LivreAudioDetailSerializer
from rest_framework.permissions import IsAdminUser

class AuteurViewSet(viewsets.ModelViewSet):
    queryset = Auteur.objects.all()
    serializer_class = AuteurSerializer
    permission_classes = [ IsAdminUser ]

class LivreAudioViewSet(viewsets.ModelViewSet):
    queryset = LivreAudio.objects.all()
    serializer_class = LivreAudioDetailSerializer
    permission_classes = [ IsAdminUser ]