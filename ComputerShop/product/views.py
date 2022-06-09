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
            data= MainboardDetailSerializer(list_mainboard, many= True)
            return Response(data.data,status.HTTP_200_OK)

class getAllRadiatorAPI(APIView):
      def get(self,request):
            list_radiator= Radiator.objects.all()
            data= RadiatorDetailSerializer(list_radiator,many= True)
            return Response(data.data,status.HTTP_200_OK)