from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer
# Create your views here.

class UserTestView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, _):
        """
        Handle GET request and return a message to confirm that the user has
        successfully logged in.

        Args:
            request: The request object

        Returns:
            Response object with a message and a status code of 200
        """
        return Response({"message": 'successfully logged in'}, status=status.HTTP_200_OK)


class RegisterView(APIView):
    permission_classes = []

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)