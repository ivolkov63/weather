from rest_framework import serializers

from DSS.models import Clothes


class ClothesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clothes
        fields = '__all__'
