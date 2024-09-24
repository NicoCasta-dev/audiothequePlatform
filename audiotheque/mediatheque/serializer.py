from rest_framework import serializers
from mediatheque.models import Auteur, LivreAudio


class AuteurSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='auteur_detail')

    class Meta:
        model : Auteur
        fields = [ 'url' ,'id', 'nom' ]

class LivreAudioListSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='livreaudio_detail')
    auteur = serializers.StringRelatedField()

    class Meta:
        model = LivreAudio
        fields = [ 'url', 'id', 'titre', 'auteur' ]

class LivreAudioDetailSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='livreaudio_detail')
    auteur = serializers.HyperlinkedRelatedField(
        view_name='auteur_detail',
        queryset=Auteur.objects.all()
    )

    class Meta:
        model = LivreAudio
        fields = [ 'url', 'id', 'auteur', 'contenu', 'duree', 'chemin_fichier' ]