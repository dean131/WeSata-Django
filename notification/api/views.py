from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny

from ..models import Notification

from .serializers import NotificationSerializer


class NotificationModelViewSet(ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = [AllowAny]