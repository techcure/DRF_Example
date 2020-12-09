from django.contrib.auth.models import User, Group
from .models import *

from django.shortcuts import get_object_or_404
from rest_framework.renderers import TemplateHTMLRenderer


from django.conf import settings
from rest_framework import viewsets
from rest_framework import permissions
from DRF_App.serializers import UserSerializer, GroupSerializer, CitySerializer
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response


class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class CityViewSet(viewsets.ModelViewSet):

    queryset = City.objects.all()
    serializer_class = CitySerializer
    permission_classes = [permissions.IsAuthenticated]