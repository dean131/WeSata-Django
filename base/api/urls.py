from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import DestinationModelViewSet 


router = DefaultRouter()
router.register('destinations', DestinationModelViewSet, basename='destination')


urlpatterns = [
    path('', include(router.urls))
]
