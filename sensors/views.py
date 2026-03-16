from .models import Sensor, Reading, Alert
from .serializers import SensorSerializer, ReadingSerializer, AlertSerializer
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .permissions import IsAdminOrReadOnly, IsSensorOperator
from django_filters.rest_framework import DjangoFilterBackend
from .filters import SensorFilter, ReadingFilter, AlertFilter

class SensorViewSet(viewsets.ModelViewSet):
    queryset = Sensor.objects.prefetch_related("readings","alerts")
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = SensorSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = SensorFilter
    
    @action(detail=True, methods=['get'])
    def readings(self, request, pk=None):
        sensor = self.get_object()
        readings = sensor.readings.all()
        serializer = ReadingSerializer(readings, many=True)
        return Response(serializer.data)
    
    @action(detail=True, methods=['get'])
    def alerts(self, request, pk=None):
        sensor = self.get_object()
        alerts = sensor.alerts.all()
        serializer = AlertSerializer(alerts, many=True)
        return Response(serializer.data)
        
    
class ReadingViewSet(viewsets.ModelViewSet):
    queryset = Reading.objects.select_related("sensor")
    permission_classes = [IsSensorOperator]
    serializer_class = ReadingSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ReadingFilter
    
    @action(detail=False, methods=['post'])
    def bulk(self, request):
        serializer = ReadingSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class AlertViewSet(viewsets.ModelViewSet):
    queryset = Alert.objects.select_related("sensor","reading")
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = AlertSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = AlertFilter
