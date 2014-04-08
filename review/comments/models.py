from django.db import models
from django.core.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic

from core.models import TimeStampedModel

# Create your models here.

class Comment(models.Model):
    comment = models.TextField()
    user = models.ForeignKey(User)
    
    # Generic Foreign Key Integration
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey('content_type', 'object_id') 
