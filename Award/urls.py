from django.urls import path, include, re_path
from . import views
from django.conf import settings
from .views import home



urlpatterns=[
  path('', views.home,name="home")
]