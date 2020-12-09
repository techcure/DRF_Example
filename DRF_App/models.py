from django.conf import settings
from django.db import models
from django.utils import timezone


class City(models.Model):
    Name = models.CharField(max_length=100, null=True, blank=True)
    Province = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.Name