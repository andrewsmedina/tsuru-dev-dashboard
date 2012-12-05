from django.db import models


class Metric(models.Model):
    name = models.CharField(max_length=255)
    url = models.URLField()


class Data(models.Model):
    metric = models.ForeignKey(Metric)
    count = models.IntegerField()
    date = models.DateTimeField()
