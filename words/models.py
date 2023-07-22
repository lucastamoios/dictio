from django.db import models
from simple_history.models import HistoricalRecords


class Word(models.Model):
    word = models.CharField(max_length=200)
    meta = models.CharField(max_length=200)
    definition = models.TextField()
    history = HistoricalRecords()