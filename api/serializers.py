from rest_framework import serializers
from .models import *

class PublicationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Publication
        fields="__all__"
        
class ChoristesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Choriste
        fields="__all__"
    
class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model=Event
        fields="__all__"
        
class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model=Attendance
        fields="__all__"
    def to_representation(self, obj):
        serializer = super().to_representation(obj)
        # serializer["choriste"] = obj.choriste.nom
        serializer["choriste"] = str(obj.choriste)
        return serializer