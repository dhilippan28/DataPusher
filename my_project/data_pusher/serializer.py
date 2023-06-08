from .models import AccountDetails, DestinationDetails
from rest_framework import serializers

class AccountDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model=AccountDetails
        fields="__all__"

class DestinationDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model=DestinationDetails
        fields="__all__"

class AccountWithDestinationSerializer(serializers.ModelSerializer):
    destinations = DestinationDetailsSerializer(source="destinationdetails_set",read_only=True,many=True)
    class Meta:
        model=AccountDetails
        fields="__all__"