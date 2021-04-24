from django.urls import path
from .views import *

app_name = "bookstore"

urlpatterns = [
    path('', index, name='index'),
    path('show/<uuid:pk>/', show, name='show')
]
