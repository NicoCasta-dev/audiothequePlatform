from rest_framework import viewsets
from .models import Auteur, LivreAudio
from .serializer import AuteurSerializer, LivreAudioListSerializer, LivreAudioDetailSerializer
from rest_framework.permissions import IsAdminUser
#from django_filters.rest_framework import DjangoFilterBanckend

class AuteurViewSet(viewsets.ModelViewSet):
    queryset = Auteur.objects.all()
    serializer_class = AuteurSerializer
    permission_classes = [ IsAdminUser ]
    # filter_backends = [ DjangoFilterBackend ]
    # filterset_fields = [ 'nom', 'prenom' ]

class LivreAudioViewSet(viewsets.ModelViewSet):
    queryset = LivreAudio.objects.all()
    serializer_class = LivreAudioDetailSerializer
    permission_classes = [ IsAdminUser ]