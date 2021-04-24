from django.urls import path
from .views import *

app_name = "bookstore"

urlpatterns = [
    path('', index, name='index'),
    path('show/<uuid:pk>/', show, name='show'),
    path('category/', create_category, name='create_category')
]
