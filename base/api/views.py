from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny

from .serializers import DestinationSerializer
from ..models import Destination


class DestinationModelViewSet(ModelViewSet):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer
    permission_classes = [AllowAny]


