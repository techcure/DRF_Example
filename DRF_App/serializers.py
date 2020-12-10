from django.contrib.auth.models import User, Group
from .models import *
from rest_framework import serializers
from django.conf import settings
from rest_framework.test import APIRequestFactory
from rest_framework.request import Request



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


# class CitySerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = City
#         fields = '__all__'


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'

    def get_city(self, obj):
        queryset = City.objects.filter(owner=obj)
        city = CitySerializer(queryset, many=True, context=self.context).data
        return city

    def update(self, instance, validated_data):
        instance.Name = validated_data.get('Name',instance.Name)
        instance.Province = validated_data.get('Province',instance.Province)

        instance.save()
        return instance

    def create(self, validated_data):
        return City.objects.create(**validated_data)