from django.db import models


class Sensor(models.Model):
    class SensorType(models.TextChoices):
        TEMPERATURE = 'temperature', 'Temperature'
        HUMIDITY = 'humidity', 'Humidity'
        PRESSURE = 'pressure', 'Pressure'
        VIBRATION = "vibration", "Vibration"
        
    name = models.CharField(max_length=100)
    sensor_type = models.CharField(
        max_length=20,
        choices=SensorType.choices
    )
    location = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['-created_at']
        
    def __str__(self) -> str:
        return self.name
    
class Reading(models.Model):
    class UnitType(models.TextChoices):
        CELCIUS = '°c','°C'
        FAHRENHEIT = '°f','°F'
        PERCENT = '%', 'percent'
        HPA = 'hPa', 'HPa'
        BAR = 'Bar', 'bar'   
    
    sensor = models.ForeignKey(to=Sensor, related_name="readings", on_delete=models.CASCADE)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    unit = models.CharField(
        max_length=10,
        choices=UnitType.choices
        )
    timestamp = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ["-timestamp"]
        
    def __str__(self) -> str:
        return f"{self.sensor} - {self.value}{self.unit}"
    
    
class Alert(models.Model):
    class AlertType(models.TextChoices):
        UPPERLIMIT = "upper_limit", "Upper Limit"
        LOWERLIMIT = "lower_limit", "Lower Limit"
        URGENT = "urgent", "Urgent"
        
    sensor = models.ForeignKey(to=Sensor, related_name="alerts", on_delete=models.CASCADE)
    reading = models.ForeignKey(to=Reading, related_name="alerts", on_delete=models.CASCADE)
    alert_type = models.CharField(
        max_length = 12,
        choices = AlertType.choices
    )
    timestamp = models.DateTimeField(auto_now_add=True)
    message = models.TextField(blank=True)
    is_resolved = models.BooleanField(default=False)
    
    class Meta:
        ordering = ["-timestamp"]
    
    def __str__(self) -> str:
        return f"{self.sensor} - {self.alert_type}"