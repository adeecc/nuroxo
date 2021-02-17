import os

from django.contrib import auth

from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed

from .models import User

MAX_PASSWORD_LENGTH = 68
MIN_PASSWORD_LENGTH = 8


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'first_name',
            'last_name',
            'phone_number',
            'profession',
            'father',
            'mother',
            'next_of_kin',
            'emergency_contact',
            'blood_group',
            'address',
        ]


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=MAX_PASSWORD_LENGTH, min_length=MIN_PASSWORD_LENGTH, write_only=True)

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
            'first_name',
            'last_name',
            'phone_number',
            'profession',
            'father',
            'mother',
            'next_of_kin',
            'emergency_contact',
            'blood_group',
            'address'
        ]

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class LoginSerializer(serializers.ModelSerializer):

    username = serializers.CharField(max_length=255)
    password = serializers.CharField(
        max_length=MAX_PASSWORD_LENGTH, min_length=MIN_PASSWORD_LENGTH, write_only=True)
    tokens = serializers.SerializerMethodField()

    def get_tokens(self, obj):
        user = User.objects.get(username=obj['username'])

        return {
            'access': user.tokens()['access'],
            'refresh': user.tokens()['refresh']
        }

    class Meta:
        model = User
        fields = ['username', 'password', 'tokens']

    def validate(self, attrs):
        username = attrs.get('username', '')
        password = attrs.get('password', '')

        user = auth.authenticate(username=username, password=password)

        if not user:
            raise AuthenticationFailed(
                'Invalid Credentials, try again.'
            )

        if not user.is_active:
            raise AuthenticationFailed(
                'Account Disabled. Contact admin'
            )

        return {
            'username': user.username,
            'tokens': user.tokens(),
        }
