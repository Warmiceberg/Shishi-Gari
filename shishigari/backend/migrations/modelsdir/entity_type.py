from django.db import models


class EntityType(models.Model):
    type = models.CharField(max_length=126, unique=True)
    priority = models.IntegerField(default=0)
    weight = models.FloatField(default=0.0)
