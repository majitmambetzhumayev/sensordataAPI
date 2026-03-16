from django.contrib import admin
from .models import Sensor, Reading, Alert

@admin.register(Sensor)
class SensorAdmin(admin.ModelAdmin):
    pass

@admin.register(Reading)
class ReadingAdmin(admin.ModelAdmin):
    pass

@admin.register(Alert)
class AlertAdmin(admin.ModelAdmin):
    pass