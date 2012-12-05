from django.db import models

from datetime import datetime

import requests


class Metric(models.Model):
    name = models.CharField(max_length=255)
    url = models.URLField()

    def fetch(self):
        result = requests.get(self.url)
        Data.objects.create(
            metric=self,
            count=result.json["open_issues"]
        )


class Data(models.Model):
    metric = models.ForeignKey(Metric)
    count = models.IntegerField()
    date = models.DateTimeField(default=datetime.now)
