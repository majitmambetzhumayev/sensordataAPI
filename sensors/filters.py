import django_filters
from .models import Sensor, Reading, Alert

class SensorFilter(django_filters.FilterSet):
    class Meta:
        model = Sensor
        fields = {
            'sensor_type': ['exact'],
            'is_active':['exact'],
            'location':['exact'],
            'created_at':['gte','lte']
        }
        
class ReadingFilter(django_filters.FilterSet):
    class Meta:
        model = Reading
        fields = {
            'sensor':['exact'],
            'unit':['exact'],
            'timestamp':['gte','lte']
        }
        
class AlertFilter(django_filters.FilterSet):
    class Meta:
        model = Alert
        fields = {
            'sensor':['exact'],
            'reading':['exact'],
            'alert_type':['exact'],
            'timestamp':['gte','lte'],
            'is_resolved':['exact']
        }