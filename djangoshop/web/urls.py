from django.urls import path
from web.views import *
from django.conf import settings

urlpatterns = [
    path('', index),
    path('user/signup', register, name='register'),
    path('categories/<slug:slug>', category),
]
