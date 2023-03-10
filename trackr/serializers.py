from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models.attendee import Attendee
from .models.user import User

class AttendeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendee
        fields = ('id', 'name', 'date', 'time')

class AttendeeWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendee
        fields = "__all__"




class UserSerializer(serializers.ModelSerializer):
   
    class Meta:
 
        model = get_user_model()
        fields = ('id', 'email', 'password')
        extra_kwargs = { 'password': { 'write_only': True, 'min_length': 1 } }


    def create(self, validated_data):
        return get_user_model().objects.create_user(**validated_data)

class UserRegisterSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=300, required=True)
    password = serializers.CharField(required=True)
    password_confirmation = serializers.CharField(required=True, write_only=True)

    def validate(self, data):
        if not data['password'] or not data['password_confirmation']:
            raise serializers.ValidationError('Please include a password and password confirmation.')

        if data['password'] != data['password_confirmation']:
            raise serializers.ValidationError('Please make sure your passwords match.')
        return data
