from django.db import models

from datetime import datetime

import requests


class Data(models.Model):
    count = models.IntegerField()
    date = models.DateTimeField(default=datetime.now)

    class Meta:
        get_latest_by = 'date'


class Metric(models.Model):
    name = models.CharField(max_length=255)
    data = models.ManyToManyField(Data, null=True, blank=True)

    class Meta:
        abstract = True


class GithubItem(Metric):
    """Example: https://api.github.com/repos/django/django/pulls?state=open"""
    url = models.URLField(max_length=1000)

    def fetch(self):
        count = 0
        page = 1
        while True:
            r = requests.get(self.url, params={
                'page': page, 'per_page': 100
            })
            c = len(r.json())
            count += c
            page += 1
            if c < 100:
                break
        return count
