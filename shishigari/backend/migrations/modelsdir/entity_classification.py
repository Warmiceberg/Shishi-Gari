from django.db import models
from .classification import Classification


class EntityClassification(models.Model):
    classification = models.ManyToManyField(Classification)
    malignant_score = models.FloatField(default=0)
