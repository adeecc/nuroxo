from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView

from authentication.models import User

from .serializers import ChatSerializer
from .scripts import NuroxoChatBot


class ChatAPIView(GenericAPIView):

    serializer_class = ChatSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = User.objects.get(id=request.user.id)

        chatbot = NuroxoChatBot.NuroxoChatBotBase(session_id=request.user.id,
                                                  name=user.get_full_name(),
                                                  blood_group=user.blood_group,
                                                  father=user.father,
                                                  mother=user.mother,
                                                  address=user.address)

        res = chatbot.reply(serializer.validated_data["message"])
        return Response(res, status=status.HTTP_200_OK)
