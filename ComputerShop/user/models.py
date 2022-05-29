from django.db import models

# Create your models here.

class Suplier(models.Model):
      name_suplier= models.CharField(max_length=255)
      address= models.CharField(max_length=255)
      phone_number= models.CharField(max_length=15)