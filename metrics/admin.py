from django.contrib import admin

from metrics.models import Metric, Data


admin.site.register(Metric)
admin.site.register(Data)
