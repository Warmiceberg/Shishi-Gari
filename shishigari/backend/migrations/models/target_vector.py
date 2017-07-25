from django.db import models
from .entity import Entity


class Action(models.Model):
    action_label = models.CharField(max_length=24, unique=True)


class Vector(models.Model):
    entity = models.ForeignKey(Entity)
    action = models.ForeignKey(Action)
    subject = models.ForeignKey(Entity)
    datetime_classified = models.DateTimeField(auto_now_add=True)
