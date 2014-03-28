from django.contrib import admin

from metrics.models import Data, Metric


admin.site.register(Data)

for MC in Metric.__subclasses__():
    admin.site.register(MC)
