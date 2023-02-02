from drf_spectacular.utils import extend_schema
from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
)
from .serializers import UserAccountSerializer

COMMON_SCHEMA_ARGS = {'tags': ['Users']}

# Create your views here.
class UsersList(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserAccountSerializer
 
    def post(self, request):
        user = User.objects.filter(email=request.data["email"])#.count()
        return (user)

class CreateUser(CreateAPIView):
    def post(self, request):
        pass


class UserEmail(APIView):
    queryset = User.objects.all()
    serializer_class = UserAccountSerializer

    def get(self, request, **kwargs):
        pk = kwargs['pk']
        user = User.objects.get(pk=pk)

        print (user)
        data = {
            'name': user.username,
            'email': user.email,
        }
        return Response(data, status = status.HTTP_200_OK)

class UpdateUser(APIView):
    def patch(self, request, *args, **kwargs):
        pass

class DeleteUser(APIView):
    def delete(self, request, *args, **kwargs):
        return Response('User account successfully deleted')