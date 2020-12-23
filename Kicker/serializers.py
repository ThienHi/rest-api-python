from rest_framework import serializers
from .models import Kicker
from datetime import date


class GetAllKickerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kicker
        fields = ('id', 'name', 'dateOfBirth', 'height', 'number', 'image',)


class KickerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kicker
        fields = ('id', 'name', 'dateOfBirth', 'height', 'number', 'image')
    name = serializers.CharField(max_length=50)
    dateOfBirth = serializers.DateField()
    height = serializers.FloatField()
    number = serializers.IntegerField()
    image = serializers.CharField(max_length=500)
