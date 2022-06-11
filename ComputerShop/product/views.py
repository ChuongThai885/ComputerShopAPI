from django.shortcuts import render
from rest_framework.views import APIView
from product.models import *
from product.serializers import *
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class getAllProductAPI(APIView):
      def get(self,request):
            list_product= Product.objects.all()
            data= ProductSerializer(list_product, many= True)
            return Response(data.data,status.HTTP_200_OK)

class getAllMainboardAPI(APIView):
      def get(self,request):
            list_mainboard= Mainboard.objects.all()
            data= MainboardSerializer(list_mainboard, many= True)
            return Response(data.data,status.HTTP_200_OK)

class getMainboardAPI(APIView):
      def get(self, request, id):
            data= {}
            _status = status.HTTP_200_OK
            try:
                  data=MainboardDetailSerializer(Mainboard.objects.get(pk=id)).data
            except:
                  data["error"]= "id not exists"
                  _status = status.HTTP_400_BAD_REQUEST
            return Response(data,_status)

class getAllRadiatorAPI(APIView):
      def get(self,request):
            list_radiator= Radiator.objects.all()
            data= RadiatorDetailSerializer(list_radiator,many= True)
            return Response(data.data,status.HTTP_200_OK)