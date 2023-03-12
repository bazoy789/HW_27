from django.db import models

class Ad(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    description = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    is_published = models.BooleanField()


class Category(models.Model):
    name = models.CharField(max_length=100)