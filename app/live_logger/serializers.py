from rest_framework import serializers
from django.contrib.auth.models import User
from . import models

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Location
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):  
    class Meta:
        model = User
        fields = '__all__'

class LogSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    location = LocationSerializer()

    class Meta:
        model = models.Log
        fields = '__all__'