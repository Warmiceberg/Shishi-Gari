from django.db import models


class LogEntry(models.Model):
    log_datetime = models.DateTimeField(auto_now_add=True)
    line_hash = models.CharField(max_length=64, unique=True)
    raw_line = models.TextField()
