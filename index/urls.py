from django.urls import path
from .views import *

urlpatterns = [
    path('', app_index, name='app_index')
]
