from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from user.models import Customer
from user.serializers import getAllCustomersSerializer
from user.serializers import RegistrationSerializers

# Create your views here.

# test cho dui nhà dui cửa thôi
class getAllUser(APIView):
      def get(self, request):
            list_user= Customer.objects.all()
            print(list_user)
            data=getAllCustomersSerializer(list_user,many=True)
            return Response(data.data,status.HTTP_200_OK)

class RegistrationAPI(APIView):
      def post(self,request):
            serializers= RegistrationSerializers(data=request.data)
            data= {}
            _status= status.HTTP_200_OK
            if serializers.is_valid():
                  account= serializers.save()
                  data['response']= 'Successfully registed new user'
                  data['username']= account.username
                  data['email']= account.email
            else:
                  data= serializers.errors
                  _status= status.HTTP_400_BAD_REQUEST
            return Response(data,_status)