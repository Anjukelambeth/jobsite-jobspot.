from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import JobseekerSerializer, RecruiterSerializer,CompanyOwnerSerializer
from rest_framework.validators import UniqueValidator

# Create your views here.
class RegisterUser(APIView):
    def post(self, request,*arg,**kargs):
        data = request.data
        user = JobseekerSerializer(data=data)

        if user.is_valid():
            user.save()
            return Response(user.data, status=status.HTTP_201_CREATED)
        else:
            return Response({'errors':user.errors},status=status.HTTP_404_NOT_FOUND)

class RegisterRecruiter(APIView):
    def post(self, request,*arg,**kargs):
        data = request.data
        user = RecruiterSerializer(data=data)

        if user.is_valid():
            user.save()
            return Response(user.data, status=status.HTTP_201_CREATED)
        else:
            return Response({'errors':user.errors},status=status.HTTP_404_NOT_FOUND)

class RegisterCompany(APIView):
    def post(self, request,*arg,**kargs):
        data = request.data
        user = CompanyOwnerSerializer(data=data)

        if user.is_valid():
            user.save()
            return Response(user.data, status=status.HTTP_201_CREATED)
        else:
            return Response({'errors':user.errors},status=status.HTTP_404_NOT_FOUND)