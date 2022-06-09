from rest_framework import serializers
from product.models import *


class MainboardDetailSerializer(serializers.ModelSerializer):
      chipset= serializers.SerializerMethodField(read_only=True)
      socket= serializers.SerializerMethodField(read_only=True)
      mainboard_form= serializers.SerializerMethodField(read_only=True)
      cpu_support= serializers.SerializerMethodField(read_only=True)
      detail_infor= serializers.SerializerMethodField(read_only=True)
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
                  'detail_infor',
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

      def get_ram_type(self, obj):
            try:
                  return obj.ram_type.memory_type
            except:
                  return None

      def get_detail_infor(self, obj):
            return ProductSerializer(obj.product).data


class CPUDetailSerializer(serializers.ModelSerializer):
      cpu_series= serializers.SerializerMethodField(read_only=True)
      cpu_generation= serializers.SerializerMethodField(read_only=True)
      socket= serializers.SerializerMethodField(read_only=True)

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
                  'detail_infor',
            )

      def get_cpu_series(self, obj):
            try:
                  return obj.cpu_series.name_series
            except:
                  return None
      
      def get_cpu_generation(self, obj):
            try:
                  return obj.cpu_generation.name_generation
            except:
                  return None

      def get_socket(self, obj):
            try:
                  return obj.socket_cpu.name_socket
            except:
                  return None

      def get_detail_infor(self, obj):
            return ProductSerializer(obj.product).data


class VGADetailSerializer(serializers.ModelSerializer):
      detail_infor= serializers.SerializerMethodField(read_only=True)
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
                  'detail_infor',
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
      
      def get_detail_infor(self, obj):
            return ProductSerializer(obj.product).data


class RAMDetailSerializer(serializers.ModelSerializer):
      detail_infor= serializers.SerializerMethodField(read_only=True)
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
                  'detail_infor',
            )
      
      def get_ram_type(self, obj):
            try:
                  return obj.ram_type.memory_type
            except:
                  return None

      def get_detail_infor(self, obj):
            return ProductSerializer(obj.product).data


class Hard_DriveDetailSerializer(serializers.ModelSerializer):
      detail_infor= serializers.SerializerMethodField(read_only=True)
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
                  'detail_infor',
            )

      def get_connection_standard(self, obj):
            try:
                  return obj.connection_standard.name_standard
            except:
                  return None
      
      def get_detail_infor(self, obj):
            return ProductSerializer(obj.product).data


class PSUDetailSerializer(serializers.ModelSerializer):
      detail_infor= serializers.SerializerMethodField(read_only=True)
      psu_performance= serializers.SerializerMethodField(read_only=True)

      class Meta:
            model= PSU
            fields =(
                  'name_psu',
                  'psu_power',
                  'psu_performance',
                  'cooling_fan_size',
                  'detail_infor',
            )
      
      def get_psu_performance(self, obj):
            try:
                  return obj.psu_performance.performance
            except:
                  return None

      def get_detail_infor(self, obj):
            return ProductSerializer(obj.product).data


class CASE_CoverDetailSerializer(serializers.ModelSerializer):
      detail_infor= serializers.SerializerMethodField(read_only=True)
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
                  'detail_infor',
            )
      
      def get_detail_infor(self, obj):
            return ProductSerializer(obj.product).data

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


class RadiatorDetailSerializer(serializers.ModelSerializer):
      socket_support= serializers.SerializerMethodField(read_only=True)
      detail_infor= serializers.SerializerMethodField(read_only=True)
      heatsink= serializers.SerializerMethodField(read_only=True)

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
                  'detail_infor',
            )
      
      def get_detail_infor(self, obj):
            return ProductSerializer(obj.product).data

      def get_heatsink(self, obj):
            try:
                  return obj.heatsink.heatsink_type
            except:
                  return None

      def get_socket_support(self,obj):
            values= Socket_Support.objects.filter(radiator_id=obj.product.id)
            data= list(values.values_list('socket_cpu', flat=True))
            values= Socket_CPU.objects.filter(pk__in= data)
            return list(values.values_list('name_socket', flat=True))


class ProductSerializer(serializers.ModelSerializer):
      manufacturer = serializers.SerializerMethodField(read_only=True)
      class Meta:
            model= Product
            fields =(
                  'id',
                  'Available_Quantity',
                  'Warranty_Period',
                  'Origin',
                  'src_img',
                  'price',
                  'manufacturer',
            )

      def get_manufacturer(self,obj):
            return obj.manufacturer.name_manufacturer