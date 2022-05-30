from django.db import models

# Create your models here.


class Manufacturer(models.Model):
      name_manufacturer= models.CharField(max_length=50)
      src_img= models.TextField(blank=True,default='')
      def __str__(self) -> str:
            return self.name_manufacturer

class Product(models.Model):
      Available_Quantity= models.IntegerField(default=0)
      # product_type= models.ForeignKey(Product_Type,on_delete=models.CASCADE)
      manufacturer= models.ForeignKey(
            Manufacturer,
            on_delete=models.CASCADE
      )
      Warranty_Period= models.IntegerField(blank=True,null=True)
      Origin= models.CharField(blank=True,null=True,max_length=50)
      src_img= models.TextField(blank=True,default='')
      price= models.FloatField(blank=True,null=True)

# mainboard 

class Socket_CPU(models.Model):
      name_socket= models.CharField(max_length=50,unique=True)
      def __str__(self) -> str:
            return self.name_manufacturer

class Chipset(models.Model):
      name_Chipset= models.CharField(max_length=50,unique=True)
      def __str__(self) -> str:
            return self.name_Chipset

class RAM_type(models.Model):
      memory_type=models.CharField(max_length=50,unique=True)
      def __str__(self) -> str:
            return self.memory_type

class Mainboard_Form(models.Model):
      name_form= models.CharField(max_length=50,unique=True)
      def __str__(self) -> str:
            return self.name_form

class Mainboard(models.Model):
      product= models.OneToOneField(
            Product,
            on_delete=models.CASCADE,
            primary_key=True
      )
      name_mainboard= models.CharField(max_length=255,unique=True)
      chipset=models.ForeignKey(
            Chipset,
            on_delete=models.CASCADE,
            blank=True,null=True
      )
      socket_cpu=models.ForeignKey(
            Socket_CPU,
            on_delete=models.CASCADE,
            blank=True,null=True
      )
      mainboard_form=models.ForeignKey(
            Mainboard_Form,
            on_delete=models.CASCADE,
            blank=True,null=True
      )
      cpu_support=models.ForeignKey(
            Manufacturer,
            on_delete=models.CASCADE,
            blank=True,null=True
      )
      ram_type=models.ForeignKey(
            RAM_type,
            on_delete=models.CASCADE,
            blank=True,null=True
      )
      maximun_ram_slot=models.IntegerField(default=1,blank=True)
      pci= models.CharField(max_length=255,blank=True,null=True)
      back_panel= models.CharField(max_length=255,blank=True,null=True)
      def __str__(self) -> str:
            return self.name_mainboard

# CPU 

class CPU_Series(models.Model):
      name_series= models.CharField(unique=True,max_length=50)
      def __str__(self) -> str:
            return self.name_series

class CPU_Generation(models.Model):
      name_generation= models.CharField(unique=True,max_length=50)
      def __str__(self) -> str:
            return self.name_generation

class CPU(models.Model):
      product= models.OneToOneField(
            Product,
            on_delete=models.CASCADE,
            primary_key=True
      )
      name_cpu= models.CharField(max_length=255,unique=True)
      cpu_series= models.ForeignKey(
            CPU_Series,
            on_delete=models.CASCADE
      )
      cpu_generation= models.ForeignKey(
            CPU_Generation,
            on_delete=models.CASCADE,
            blank=True,null=True
      )
      cpu_type= models.CharField(max_length=50,unique=True)
      socket_cpu= models.ForeignKey(
            Socket_CPU,
            on_delete=models.CASCADE,
            blank=True,null=True
      )
      number_of_core= models.IntegerField(blank=True,null=True)
      number_of_threads= models.IntegerField(blank=True,null=True)
      processing_speed= models.TextField(blank=True,null=True)
      cache_cpu= models.CharField(max_length=50,blank=True,null=True)
      tdp= models.CharField(max_length=50,blank=True,null=True)
      def __str__(self) -> str:
            return self.name_cpu

# Card đồ họa 

class GPU(models.Model):
      name_gpu= models.CharField(unique=True,max_length=50)
      def __str__(self) -> str:
            return self.name_gpu

class Memory_Standard(models.Model):
      name_standard= models.CharField(unique=True,max_length=50)
      def __str__(self) -> str:
            return self.name_standard

class VGA(models.Model):
      product= models.OneToOneField(
            Product,
            on_delete=models.CASCADE,
            primary_key=True
      )
      name_vga= models.CharField(max_length=255,unique=True)
      def __str__(self) -> str:
            return self.name_vga

# RAM

class RAM(models.Model):
      product= models.OneToOneField(
            Product,
            on_delete=models.CASCADE,
            primary_key=True
      )
      name_ram= models.CharField(max_length=255,unique=True)
      ram_type= models.ForeignKey(
            RAM_type,
            on_delete=models.CASCADE,
            blank=True,null=True
      )
      capacity= models.CharField(max_length=20,blank=True,null=True)
      speed= models.IntegerField(blank=True,null=True)
      quantity_in_pack= models.IntegerField(blank=True,null=True)
      rbg= models.BooleanField(blank=True,default=False,)
      def __str__(self) -> str:
            return self.name_ram

# Ổ cứng 

class Connection_standard(models.Model):
      name_standard= models.CharField(unique=True,max_length=50)
      def __str__(self) -> str:
            return self.name_standard

class Hard_Drive(models.Model):
      product= models.OneToOneField(
            Product,
            on_delete=models.CASCADE,
            primary_key=True
      )
      name_hard_drive= models.CharField(max_length=255,unique=True)
      capacity= models.CharField(max_length=20,blank=True,null=True)
      ssd= models.BooleanField(default=False,blank=True)
      connection_standard= models.ForeignKey(
            Connection_standard,
            on_delete=models.CASCADE,
            blank=True,null=True
      )
      read_speed= models.IntegerField(blank=True,null=True)
      write_speed= models.IntegerField(blank=True,null=True)
      def __str__(self) -> str:
            return self.name_hard_drive

# Nguồn máy tính 

class PSU_Performance(models.Model):
      performance= models.CharField(unique=True,max_length=50)
      def __str__(self) -> str:
            return self.performance

class PSU(models.Model):
      product= models.OneToOneField(
            Product,
            on_delete=models.CASCADE,
            primary_key=True
      )
      name_psu= models.CharField(max_length=255,unique=True)
      psu_power= models.IntegerField(blank=True,null=True)
      psu_performance= models.ForeignKey(
            PSU_Performance,
            on_delete=models.CASCADE,
            blank=True,null=True
      )
      cooling_fan_size= models.CharField(max_length=255,blank=True,null=True)
      def __str__(self) -> str:
            return self.name_psu

# Vỏ máy 

class CaseType(models.Model):
      name_case_type= models.CharField(unique=True,max_length=50)
      def __str__(self) -> str:
            return self.name_case_type

class Colors(models.Model):
      name_color= models.CharField(unique=True,max_length=50)
      def __str__(self) -> str:
            return self.name_color

class CASE_Cover(models.Model):
      product= models.OneToOneField(
            Product,
            on_delete=models.CASCADE,
            primary_key=True
      )
      name_case_cover= models.CharField(max_length=255,unique=True)
      case_type= models.ForeignKey(
            CaseType,
            on_delete=models.CASCADE,
            blank=True,null=True
      )
      material= models.TextField(blank=True,null=True)
      size= models.CharField(max_length=50,blank=True,null=True)
      rgb= models.BooleanField(blank=True,null=True)
      color=models.ForeignKey(
            Colors,
            on_delete=models.CASCADE,
            blank=True,null=True
      )
      def __str__(self) -> str:
            return self.name_case_cover

class Mainboard_Support(models.Model):
      case_cover= models.ForeignKey(
            CASE_Cover,
            on_delete= models.CASCADE
      )
      mainboard_form= models.ForeignKey(
            Mainboard_Form,
            on_delete= models.CASCADE
      )
      class Meta:
            constraints = [
                  models.UniqueConstraint(
                        fields=['case_cover', 'mainboard_form'], name='unique_casecover_mainboardform_combination'
                  )
            ]

# Quạt tản nhiệt 

class Heatsink(models.Model):
      heatsink_type= models.CharField(unique=True,max_length=50)
      def __str__(self) -> str:
            return self.heatsink_type

class Radiator(models.Model):
      product= models.OneToOneField(
            Product,
            on_delete=models.CASCADE,
            primary_key=True
      )
      name_radiator= models.CharField(max_length=255,unique=True)
      heatsink= models.ForeignKey(
            Heatsink,
            on_delete=models.CASCADE,
            blank=True,null=True
      )
      material= models.TextField(blank=True,null=True)
      wattage= models.FloatField(blank=True,null=True)
      Speed= models.IntegerField(blank=True,null=True)
      rgb=models.BooleanField(blank=True,null=True)
      size=models.CharField(max_length=50,blank=True,null=True)
      def __str__(self) -> str:
            return self.name_radiator

class Socket_Support(models.Model):
      radiator= models.ForeignKey(
            Radiator,
            on_delete=models.CASCADE
      )
      socket_cpu=models.ForeignKey(
            Socket_CPU,
            on_delete=models.CASCADE
      )
      class Meta:
            constraints = [
                  models.UniqueConstraint(
                        fields=['radiator', 'socket_cpu'], name='unique_radiator_socketcpu_combination'
                  )
            ]