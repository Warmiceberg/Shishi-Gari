from django.db import models


class IngestedFile(models.Model):
    """
    This is the model for each file container, all files that are ingested will be here
    """
    ingested_file = models.FileField()
    filename = models.CharField(max_length=128)
    datetime_classified = models.DateTimeField(auto_now_add=True)
    datetime_started_processing = models.DateTimeField(null=True)
    datetime_processed = models.DateTimeField(null=True)
    processed = models.BooleanField(default=False)
    progress = models.FloatField(default=0.0)
    ran_into_error = models.BooleanField(default=False)
