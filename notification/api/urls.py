from django.urls import path, include

from .views import NotificationModelViewSet

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("notifications", NotificationModelViewSet, basename="notification")

urlpatterns = [
    path("", include(router.urls)),
]