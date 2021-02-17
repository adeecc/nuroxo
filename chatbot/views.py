from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView

from .serializers import ChatSerializer

class ChatAPIView(GenericAPIView):

    serializer_class = ChatSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        res = serializer.validated_data
        return Response(res, status=status.HTTP_200_OK)