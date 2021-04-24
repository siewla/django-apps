from bookstore.models import Book
from django.db import models
import uuid
from bookstore.models import Book

# Create your models here.


class Review(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200, null=False)
    review = models.TextField(null=False)
    book = models.ForeignKey(
        Book, on_delete=models.CASCADE, related_name="reviews")
