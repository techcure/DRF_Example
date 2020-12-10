
from django.contrib import admin

from django.conf import settings

from django.urls import include, path
from rest_framework import routers
from DRF_App import views
from DRF_App.views import *
from django.conf.urls import url


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'City', views.CityViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('get-data/', views.getdata),
    path('hello-data/', views.hello_world),
    path('city-view/', CityList.as_view()),
    path('city-detail/<int:pk>/', CityDetail.as_view()),
]