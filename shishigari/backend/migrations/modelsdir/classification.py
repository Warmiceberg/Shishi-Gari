from django.db import models
from .classification_label import ClassificationLabel


class Classification(models.Model):
    classification = models.ForeignKey(ClassificationLabel)
    datetime_classified = models.DateTimeField(auto_now_add=True)
