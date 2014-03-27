from django.db import models

from datetime import datetime

import requests


class Data(models.Model):
    count = models.IntegerField()
    date = models.DateTimeField(default=datetime.now)


class Metric(models.Model):
    name = models.CharField(max_length=255)
    data = models.ManyToManyField(Data)

    class Meta:
        abstract = True
