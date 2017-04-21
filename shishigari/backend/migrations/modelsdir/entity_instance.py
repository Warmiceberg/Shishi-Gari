from django.db import models
from .entity_type import EntityType


class EntityInstance(models.Model):
    type = models.ForeignKey(EntityType)
    label = models.CharField(max_length=252)

    class Meta:
        unique_together = ('type', 'label',)
