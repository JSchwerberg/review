from django.db import models
from django.db.models import ForeignKey, CharField, TextField, ManyToManyField, IntegerField
from django.contrib.auth.models import User

from core.models import TimeStampedModel

# Create your models here.

class RatableField(models.Model):
    name = CharField(max_length=20)
    desc = TextField()


class Category(models.Model):
    name = CharField(max_length=50)
    ratable_fields = ManyToManyField(RatableField)


class Item(models.Model):
    name = CharField(max_length=50)
    category = ForeignKey(Category)
    description = TextField()


class Rating(TimeStampedModel):
    user = ForeignKey(User)
    item = ForeignKey(Item)
    rated_field = .ForeignKey(RatableField)
    score = IntegerField()


class Review(TimeStampedModel):
    user = ForeignKey(User)
    item = ForeignKey(Item)
    review = TextField()
    ratings = ManyToManyField(Rating)


