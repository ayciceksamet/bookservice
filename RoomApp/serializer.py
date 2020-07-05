from rest_framework import serializers
from .models import Room, IntervalData
import time

class IntervalSerializer(serializers.ModelSerializer):

    class Meta:
        model = IntervalData
        fields = ['__all__']

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['__all__']
