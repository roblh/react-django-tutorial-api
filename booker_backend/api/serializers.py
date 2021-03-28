from rest_framework import serializers
from .models import EventsNames, EventParticipants, EventTimes, EventLocations 
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User 
        fields = ('id', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    #need to override built in create, where password is stored in plaintext and create our own to hash it
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user

class EventNamesSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventNames 
        fields = ('id', 'name', 'userId', 'eventId')

class EventParticipantsSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventParticipants 
        fields = ('id', 'attendee', 'userAdmitted', 'eventAdmin', 'userId', 'eventId')

class EventTimesSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventTimes 
        fields = ('id', 'time', 'userId', 'eventId')

class EventLocationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventLocations 
        fields = ('id', 'location', 'userId', 'eventId')

class EventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventLocations 
        fields = ('id', 'finalEventName', 'finalEventParticipants', 'finalEventTime', 'finalEventLocation', 'votingClosed', 'userId', 'eventId')
