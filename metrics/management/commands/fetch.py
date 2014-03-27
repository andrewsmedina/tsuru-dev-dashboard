# -*- coding: utf-8 -*-
from django.core.management.base import NoArgsCommand

from ..models import Metric


class Command(NoArgsCommand):

    def handle_noargs(self, **options):
        for MC in Metric.__subclasses__():
            for metric in MC.objects.all():
                metric.data.create(measurement=metric.fetch())
