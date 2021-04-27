from django.urls import path
from accounts.views import *

app_name = "accounts"

urlpatterns = [
    path('register/', view_register, name="register"),
    path('login/', view_login, name="login"),
    path('logout/', view_logout, name="logout"),

]
