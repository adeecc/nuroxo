from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.
class IndexView(APIView):

    def get(self, request, format=None):

        data = {
            "body": "REST Motherfucker, do you speak it!"
        }

        return Response(data, status=status.HTTP_200_OK) 