from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
import uuid


class User(AbstractUser):
    pass


class Profile(models.Model):
    id = models.UUIDField(  # new
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    user = models.OneToOneField(
        User, related_name='profile', on_delete=models.CASCADE)
    city = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
