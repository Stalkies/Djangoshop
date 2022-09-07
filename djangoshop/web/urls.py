from django.urls import path
from web.views import index, category
from django.conf import settings

urlpatterns = [
    path('', index),
    path('categories/<slug:slug>', category),
]
