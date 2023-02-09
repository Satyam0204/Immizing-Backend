from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import *

class FNSerializer(serializers.ModelSerializer):
    class Meta:
        model=ForeignNationalInfo
        fields='__all__'

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model=Address
        fields='__all__'