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
    title = CharField(
        max_length=20
    )
    pages = IntegerField(
        default=0
    )
    description = CharField(
        max_length=100,
        default=0
    )
    author = CharField(
        max_length=10
    )
