from django.db import models

# Create your models here.


class Manufacturer(models.Model):

      name_manufacturer= models.CharField(max_length=20)

      def __str__(self) -> str:
            return self.name_manufacturer

class Product_Type(models.Model):

      name_type= models.CharField(max_length=20)
      
      def __str__(self) -> str:
            return self.name_type

class Product(models.Model):

      Available_Quantity= models.IntegerField(default=0)
      product_type= models.ForeignKey(Product_Type,on_delete=models.CASCADE)
      manufacturer= models.ForeignKey(Manufacturer,on_delete=models.CASCADE)
      Warranty_Period= models.IntegerField(null=True)
      Origin= models.CharField(max_length=30)
      src_img= models.TextField(null=True,blank=True,default='')
      price= models.FloatField()