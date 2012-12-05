# -*- coding: utf-8 -*-
from django.core.management.base import NoArgsCommand

from metrics.models import Metric


class Command(NoArgsCommand):

    can_import_settings = True

    def handle_noargs(self, **options):
        for metric in Metric.objects.all():
            metric.fetch()
        return u"ok!"
