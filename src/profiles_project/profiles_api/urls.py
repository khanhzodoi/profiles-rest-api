from django.urls import path,re_path
from django.urls import include

from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, basename='hello-viewset')

urlpatterns = [
    re_path(r'^hello-view/', views.HelloAPIView.as_view()),
    re_path(r'', include(router.urls))
]