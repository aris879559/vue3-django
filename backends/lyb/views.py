from django.shortcuts import render

# Create your views here.
# from django.contrib.auth.models import Group, User
# from tutorial.quickstart.serializers import GroupSerializer, UserSerializer
from rest_framework import permissions, viewsets
from .models import Lyb
from .serializers import LybSerializer

class LybViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Lyb.objects.all().order_by('-posttime')
    serializer_class = LybSerializer
    # permission_classes = [permissions.IsAuthenticated]