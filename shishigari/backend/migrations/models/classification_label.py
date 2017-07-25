from django.db import models


class ClassificationLabel(models.Model):
    label = models.CharField(max_length=126, unique=True)
