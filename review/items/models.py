from django.db import models
from django.db.models import (ForeignKey, CharField, TextField, ManyToManyField, 
                             IntegerField, ImageField, PositiveIntegerField)
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.generic import GenericForeignKey, GenericRelation

from core.models import TimeStampedModel
from core.managers import path_and_rename

# Create your models here.

class Image(models.Model):
    image = ImageField(upload_to=path_and_rename('path/here/'))
    description = CharField(max_length=255)
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

class RatableField(models.Model):
    name = CharField(max_length=20)
    desc = TextField()


class Category(models.Model):
    name = CharField(max_length=50)
    ratable_fields = ManyToManyField(RatableField)
    image = ImageField(upload_to=path_and_rename('path/here/'))

class Item(models.Model):
    name = CharField(max_length=50)
    category = ForeignKey(Category)
    description = TextField()
    comments = generic.GenericRelation(Comment)
    images = generic.GenericRelation(Image)

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


