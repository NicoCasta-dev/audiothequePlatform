from rest_framework import serializers
from .models import Avis

class AvisSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='avis_detail')
    utilisateur = serializers.StringRelatedField()
    livre_audio = serializers.HyperlinkedRelatedField(
        view_name='livreaudio_detail',
        read_only=True
    )

    class Meta:
        model = Avis
        fields = [ 'url', 'id', 'utilisateur', 'livre_audio', 'note', 'commentaire' ]