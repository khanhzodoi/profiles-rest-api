from django.urls import path,re_path

from . import views


urlpatterns = [
    re_path(r'^hello-view/', views.HelloAPIView.as_view())
]