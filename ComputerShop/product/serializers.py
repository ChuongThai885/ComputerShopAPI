from rest_framework import serializers
from product.models import *


class MainboardSerializer(serializers.ModelSerializer):
      cpu_support= serializers.SerializerMethodField(read_only=True)
      socket= serializers.SerializerMethodField(read_only=True)
      mainboard_form= serializers.SerializerMethodField(read_only=True)
      chipset= serializers.SerializerMethodField(read_only=True)

      class Meta:
            model= Mainboard
            fields =(
                  'name_mainboard',
                  'cpu_support',
                  'socket',
                  'mainboard_form',
                  'chipset',
                  'maximun_ram_slot',
            )
      
      def get_chipset(self, obj):
            try:
                  return obj.chipset.name_Chipset
            except:
                  return None

      def get_socket(self, obj):
            try:
                  return obj.socket_cpu.name_socket
            except:
                  return None

      def get_mainboard_form(self, obj):
            try:
                  return obj.mainboard_form.name_form
            except:
                  return None

      def get_cpu_support(self, obj):
            try:
                  return obj.cpu_support.name_manufacturer
            except:
                  return None


class MainboardDetailSerializer(MainboardSerializer):
      ram_type= serializers.SerializerMethodField(read_only=True)

      class Meta:
            model= Mainboard
            fields =(
                  'name_mainboard',
                  'chipset',
                  'socket',
                  'mainboard_form',
                  'cpu_support',
                  'ram_type',
                  'maximun_ram_slot',
                  'pci',
                  'back_panel',
            )

      def get_ram_type(self, obj):
            try:
                  return obj.ram_type.memory_type
            except:
                  return None


class CPUSerializer(serializers.ModelSerializer):
      cpu_series= serializers.SerializerMethodField(read_only=True)
      cpu_generation= serializers.SerializerMethodField(read_only=True)
      socket= serializers.SerializerMethodField(read_only=True)
      
      class Meta:
            model= CPU
            fields= (
                  'name_cpu',
                  'cpu_series',
                  'cpu_generation',
                  'socket',
                  'number_of_core',
                  'number_of_threads',
                  'tdp',
            )

      def get_cpu_series(self, obj):
            try:
                  return str(obj.cpu_series.manufacturer)+ " "+ obj.cpu_series.name_series
            except:
                  return None
      
      def get_cpu_generation(self, obj):
            try:
                  return str(obj.cpu_series.manufacturer)+ " "+ obj.cpu_generation.name_generation
            except:
                  return None

      def get_socket(self, obj):
            try:
                  return obj.socket_cpu.name_socket
            except:
                  return None


class CPUDetailSerializer(CPUSerializer):

      class Meta:
            model= CPU
            fields= (
                  'name_cpu',
                  'cpu_series',
                  'cpu_generation',
                  'cpu_type',
                  'socket',
                  'number_of_core',
                  'number_of_threads',
                  'processing_speed',
                  'cache_cpu',
                  'tdp',
            )


class VGADetailSerializer(serializers.ModelSerializer):
      gpu= serializers.SerializerMethodField(read_only=True)
      memory_standard= serializers.SerializerMethodField(read_only=True)

      class Meta:
            model= VGA
            fields =(
                  'name_vga',
                  'gpu',
                  'memory_standard',
                  'capacity',
                  'oc_mode',
                  'gaming_mode',
                  'microwave',
                  'number_of_processing_units',
                  'radiators',
            )

      def get_gpu(self, obj):
            try:
                  return obj.gpu.name_gpu
            except:
                  return None

      def get_memory_standard(self, obj):
            try:
                  return obj.memory_standard.name_standard
            except:
                  return None


class RAMDetailSerializer(serializers.ModelSerializer):
      ram_type= serializers.SerializerMethodField(read_only=True)

      class Meta:
            model= RAM
            fields =(
                  'name_ram',
                  'ram_type',
                  'capacity',
                  'speed',
                  'quantity_in_pack',
                  'rbg',
            )
      
      def get_ram_type(self, obj):
            try:
                  return obj.ram_type.memory_type
            except:
                  return None


class Hard_DriveDetailSerializer(serializers.ModelSerializer):
      connection_standard= serializers.SerializerMethodField(read_only=True)

      class Meta:
            model= Hard_Drive
            fields =(
                  'name_hard_drive',
                  'capacity',
                  'ssd',
                  'connection_standard',
                  'read_speed',
                  'write_speed',
            )

      def get_connection_standard(self, obj):
            try:
                  return obj.connection_standard.name_standard
            except:
                  return None


class PSUDetailSerializer(serializers.ModelSerializer):
      psu_performance= serializers.SerializerMethodField(read_only=True)

      class Meta:
            model= PSU
            fields =(
                  'name_psu',
                  'psu_power',
                  'psu_performance',
                  'cooling_fan_size',
            )
      
      def get_psu_performance(self, obj):
            try:
                  return obj.psu_performance.performance
            except:
                  return None


class CASE_CoverDetailSerializer(serializers.ModelSerializer):
      mainboard_support= serializers.SerializerMethodField(read_only=True)
      case_type= serializers.SerializerMethodField(read_only=True)
      color= serializers.SerializerMethodField(read_only=True)

      class Meta:
            model= CASE_Cover
            fields =(
                  'name_case_cover',
                  'case_type',
                  'material',
                  'size',
                  'rgb',
                  'color',
                  'mainboard_support',
            )

      def get_mainboard_support(self, obj):
            values= Mainboard_Support.objects.filter(case_cover_id=obj.product.id)
            data= list(values.values_list('mainboard_form', flat=True))
            values= Mainboard_Form.objects.filter(pk__in= data)
            return list(values.values_list('name_form', flat=True))

      def get_case_type(self, obj):
            try:
                  return obj.case_type.name_case_type
            except:
                  return None

      def get_color(self, obj):
            try:
                  return obj.color.name_color
            except:
                  return None


class RadiatorSerializer(serializers.ModelSerializer):
      heatsink= serializers.SerializerMethodField(read_only=True)

      class Meta:
            model= Radiator
            fields =(
                  'name_radiator',
                  'heatsink',
                  'Speed',
                  'rgb',
                  'size',
            )

      def get_heatsink(self, obj):
            try:
                  return obj.heatsink.heatsink_type
            except:
                  return None


class RadiatorDetailSerializer(RadiatorSerializer):
      socket_support= serializers.SerializerMethodField(read_only=True)

      class Meta:
            model= Radiator
            fields =(
                  'name_radiator',
                  'heatsink',
                  'material',
                  'wattage',
                  'Speed',
                  'rgb',
                  'size',
                  'socket_support',
            )

      def get_socket_support(self,obj):
            values= Socket_Support.objects.filter(radiator_id=obj.product.id)
            data= list(values.values_list('socket_cpu', flat=True))
            values= Socket_CPU.objects.filter(pk__in= data)
            return list(values.values_list('name_socket', flat=True))


class ProductSerializer(serializers.ModelSerializer):
      manufacturer = serializers.SerializerMethodField(read_only=True)
      product_type= serializers.SerializerMethodField(read_only=True)
      detail_infor= serializers.SerializerMethodField(read_only=True)

      class Meta:
            model= Product
            fields =(
                  'id',
                  'product_type',
                  'manufacturer',
                  'src_img',
                  'price',
                  'Available_Quantity',
                  'Warranty_Period',
                  'Origin',
                  'detail_infor',
            )

      def get_manufacturer(self,obj):
            return obj.manufacturer.name_manufacturer

      def get_product_type(self, obj):
            return obj.product_type.name_type

      def get_detail_infor(self, obj):
            _type= obj.product_type.name_type
            if _type=='Mainboard':
                  return MainboardDetailSerializer(obj.mainboard).data
            elif _type== 'CPU':
                  return CPUSerializer(obj.cpu).data
            elif _type== 'VGA':
                  return None
            elif _type== 'RAM':
                  return None
            elif _type== 'Hard_Drive':
                  return None
            elif _type== 'PSU':
                  return None
            elif _type== 'CASE_Cover':
                  return None
            elif _type== 'Radiator':
                  return RadiatorSerializer(obj.radiator).data
            else:
                  return None

class ProductDetailSerializer(ProductSerializer):

      def get_detail_infor(self, obj):
            _type= obj.product_type.name_type
            if _type=='Mainboard':
                  return MainboardDetailSerializer(obj.mainboard).data
            elif _type== 'CPU':
                  return CPUDetailSerializer(obj.cpu).data
            elif _type== 'VGA':
                  return None
            elif _type== 'RAM':
                  return None
            elif _type== 'Hard_Drive':
                  return None
            elif _type== 'PSU':
                  return None
            elif _type== 'CASE_Cover':
                  return None
            elif _type== 'Radiator':
                  return RadiatorDetailSerializer(obj.radiator).data
            else:
                  return None