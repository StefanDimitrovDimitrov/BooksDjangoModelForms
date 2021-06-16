"""
•	title – CharField with max-length of 20
•	pages – IntegerField with default value of 0
•	description – CharField with max length of 100 and empty string as a default value
•	author – CharField with max length of 20



"""

from django.db import models

# Create your models here.
from django.db.models import CharField, IntegerField


class BookModel(models.Model):
    title = models.CharField(
        max_length=20
    )
    pages = models.IntegerField(
    )
    description = models.TextField(
        max_length=100,
        default=''
    )
    author = models.CharField(
        max_length=10
    )
