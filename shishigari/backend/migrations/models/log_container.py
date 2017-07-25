import jsonfield
from django.db import models
from .entity import Entity


class LogContainer(models.Model):
    container_hash = models.CharField(max_length=64, unique=True)
    entities = models.ManyToManyField(Entity, through='logcontainertoentitymap')
    json_representation = jsonfield.JSONField(default={})


class Relationship(models.Model):
    models.CharField(max_length=128, unique=True)


class LogContainerToEntityMap(models.Model):
    models.ForeignKey(Entity)
    models.ForeignKey(LogContainer)
    models.ForeignKey(Relationship)
