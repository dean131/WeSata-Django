from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny

from .serializers import UserSerializer
from ..models import User


class UserModelViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


