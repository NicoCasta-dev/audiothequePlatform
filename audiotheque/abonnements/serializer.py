from rest_framework import serializers
from .models import Abonnement, Transaction

class AbonnementSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='abonnement_detail')
    utilisateur = serializers.HyperlinkedRelatedField(
        view_name='user_detail',
        read_only=True
    )

    class Meta:
        model : Abonnement
        fields = [ 'url', 'id', 'utilisateur', 'date_debut', 'date_fin', 'statut' ]

class TransactionSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='transaction_detail')
    utilisateur = serializers.HyperlinkedRelatedField(
        view_name='user_detail',
        read_only=True
    )

    class Meta:
        model = Transaction
        fields = ['url', 'id', 'utilisateur', 'abonnement', 'montant', 'type_transaction', 'date_transaction']
