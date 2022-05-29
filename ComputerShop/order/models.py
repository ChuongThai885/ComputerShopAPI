from zoneinfo import available_timezones
from django.db import models
from product.models import Product
from user.models import Suplier
# Create your models here.


class Payment(models.Model):

      payment_type= models.CharField(max_length=20)
      available= models.BooleanField(default=True)
      def __str__(self) -> str:
            return self.payment_type

class Orders(models.Model):

      # ID_Customer
      suplier= models.ForeignKey(Suplier,on_delete=models.CASCADE)
      delivery_address= models.CharField(max_length=255)
      payment = models.ForeignKey(Payment,on_delete=models.CASCADE)

class Orders_detail(models.Model):
      
      orders = models.ForeignKey(Orders,on_delete=models.CASCADE)
      product= models.ForeignKey(Product,on_delete=models.CASCADE)
      number_product= models.IntegerField(default=1)
      price= models.FloatField()
      discount= models.FloatField()

      class Meta:
            constraints = [
                  models.UniqueConstraint(
                        fields=['orders', 'product'], name='unique_orders_productinfo_combination'
                  )
            ]