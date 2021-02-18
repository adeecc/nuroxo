from rest_framework import serializers

from .scripts import NuroxoChatBot

class ChatSerializer(serializers.Serializer):
    timestamp = serializers.DateTimeField()
    message = serializers.CharField(min_length=1)

    def validate(self, attrs):
        return super().validate(attrs)