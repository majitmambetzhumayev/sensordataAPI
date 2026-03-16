from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import SensorViewSet, ReadingViewSet, AlertViewSet

router = DefaultRouter()
router.register('sensors', SensorViewSet)
router.register('readings', ReadingViewSet)
router.register('alerts', AlertViewSet)

urlpatterns = [
    path('', include(router.urls)),
]