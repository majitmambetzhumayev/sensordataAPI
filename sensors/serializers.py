from rest_framework import serializers
from .models import Sensor, Reading, Alert

class SensorSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Sensor
        fields = ['id','name','sensor_type','created_at','location','is_active']
        read_only_fields = ['id','created_at']
        
class ReadingSerializer(serializers.ModelSerializer):
    sensor_name = serializers.CharField(source='sensor.name', read_only=True)
    class Meta:
        model = Reading
        fields = ['id','sensor','sensor_name','timestamp','value','unit']
        read_only_fields = ['id','timestamp']
        
class AlertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alert
        fields = ['id','sensor','reading','alert_type','timestamp','message','is_resolved']
        read_only_fields = ['id','timestamp']