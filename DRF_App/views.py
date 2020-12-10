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
from django.http import JsonResponse
from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView


class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):

    queryset = Group.objects.all()
    serializer_class = GroupSerializer



class CityViewSet(viewsets.ModelViewSet):

    queryset = City.objects.all()
    serializer_class = CitySerializer

def getdata(request):
    return JsonResponse({"name": "Oppppp"})

@api_view(['GET', 'POST'])
def hello_world(request):
    if request.method == 'POST':
        return Response({"message": "Got some data!", "data": request.data})
    return Response({"message": "Hello, world!"})


class CityList(APIView):

    def get(self, request, format=None):
        city_obj = City.objects.all()
        serializer = CitySerializer(city_obj, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CityDetail(APIView):

    def get_object(self, pk, *args, **kwargs):
        try:
            return City.objects.get(pk=pk)
        except City.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None, *args, **kwargs):
        city_obj = self.get_object(pk)
        serializer = CitySerializer(city_obj)
        return Response(serializer.data)

    def put(self, request, pk, format=None, *args, **kwargs):
        city_obj = self.get_object(pk)
        serializer = CitySerializer(city_obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None, *args, **kwargs):
        city_obj = self.get_object(pk)
        city_obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)