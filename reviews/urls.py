from django.urls import path
from .views import *

app_name = 'reviews'

urlpatterns = [
    path('<uuid:book>/', create, name='create')
]

# reviews:index
