from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    # path('show/<uuid:pk>', show, name='show')
]
