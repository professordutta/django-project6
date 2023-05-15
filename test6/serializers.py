from rest_framework import serializers
from .models import Olympics

class MedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Olympics
        fields = ['country_name', 'medals_won']
