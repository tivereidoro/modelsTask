from typing import Text
from django.db import models
from django.conf import settings

# Create models here.


class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    Author = models.ForeignKey()
    Created_date = models.DateTimeField
    Published_date = models.DateTimeField

    def __str__(self) -> str:
        return self().__str__()
