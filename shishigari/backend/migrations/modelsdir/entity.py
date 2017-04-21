from django.db import models
from .entity_instance import EntityInstance
from .entity_classification import EntityClassification


class Entity(models.Model):
    entity_instance = models.ManyToManyField(EntityInstance)
    classification = models.ForeignKey(EntityClassification)
    #ownership field
