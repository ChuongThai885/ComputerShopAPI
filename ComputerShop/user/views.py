from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

from user.models import Customer
from user.serializers import getAllCustomersSerializer
from user.serializers import RegistrationSerializers,getUserInforSerializers

from rest_framework_simplejwt.tokens import RefreshToken

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
                  refresh= RefreshToken.for_user(account)
                  data['refresh']= str(refresh)
                  data['access']= str(refresh.access_token)
            else:
                  data= serializers.errors
                  _status= status.HTTP_400_BAD_REQUEST
            return Response(data,_status)

class getUserInfor(APIView):
      permission_classes=[permissions.IsAuthenticated]

      def get(self,request):
            infor= Customer.objects.get(pk=request.user.id)
            data= {}
            _status= status.HTTP_200_OK
            try:
                  data= getUserInforSerializers(infor).data
            except:
                  data["error"]= "an error has occur"
            return Response(data,_status)