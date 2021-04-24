from django.db import models
import uuid
# Create your models here.


class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200, null=False)

    def __str__(self):
        return self.name


class Book(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200, null=False)
    author = models.CharField(max_length=200, null=False)
    description = models.TextField()
    published_year = models.IntegerField(null=False)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    cover = models.ImageField(upload_to='uploads/%Y/%m/%d')
    categories = models.ManyToManyField(Category, related_name='bookstore')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


def __str__(self):
    return self.title
