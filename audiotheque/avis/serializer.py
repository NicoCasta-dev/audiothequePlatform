from rest_framework import serializers
from .models import Avis

class AvisSerializer(serializers.HyperlinkedModelSerializer):

    utilisateur = serializers.StringRelatedField()
    # livre_audio = serializers.HyperlinkedRelatedField(
    #     view_name='livreaudio-detail',
    #     read_only=True
    # )

    class Meta:
        model = Avis
        fields = [ 'utilisateur', 'livre_audio', 'note', 'commentaire' ]