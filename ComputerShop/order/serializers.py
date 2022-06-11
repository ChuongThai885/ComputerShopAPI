from rest_framework import serializers
from order.models import *

class getOrderSerializer(serializers.ModelSerializer):
      payment= serializers.SerializerMethodField(read_only=True)
      class Meta:
            model= Orders
            fields =(
                  'id',
                  'order_date',
                  'total_prices',
                  'payment',
            )
      
      def get_payment(self, obj):
            return obj.payment.payment_type


class getOrderDetailSerializer(serializers.ModelSerializer):
      name_customer= serializers.SerializerMethodField(read_only=True)
      payment= serializers.SerializerMethodField(read_only=True)

      class Meta:
            model= Orders
            fields =(
                  'name_customer',
                  'delivery_address',
                  'order_date',
                  'total_prices',
                  'payment',
            )
      
      def get_payment(self, obj):
            return obj.payment.payment_type

      def get_name_customer(self, obj):
            try: 
                  return str(obj.customer.first_name)+" "+ str(obj.customer.last_name)
            except:
                  return None


class AddNewOrderSerializer(serializers.ModelSerializer):
      pass