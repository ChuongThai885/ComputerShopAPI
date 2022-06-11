from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

from order.models import *
from .serializers import getOrderSerializer,getOrderDetailSerializer

# Create your views here.


class getOrdersAPI(APIView):
      permission_classes=[permissions.IsAuthenticated]

      def get(self, request):
            list= Orders.objects.filter(customer_id=request.user.id)
            data={}
            _status= status.HTTP_200_OK
            data= getOrderSerializer(list,many=True).data
            return Response(data,_status)


class getOrderDetailAPI(APIView):
      permission_classes=[permissions.IsAuthenticated]

      def get(self, request, id_order):
            list= Orders.objects.filter(customer_id=request.user.id)
            data={}
            _status= status.HTTP_200_OK
            try:
                  d= list.get(pk=id_order)
                  data= getOrderDetailSerializer(d).data
            except:
                  data['error']= 'Orders does not exist'
                  _status= status.HTTP_400_BAD_REQUEST
            return Response(data,_status)