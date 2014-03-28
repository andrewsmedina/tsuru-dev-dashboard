from metrics.models import Metric

from django.shortcuts import render


def index(request):
    metrics = []
    for MC in Metric.__subclasses__():
        metrics.extend(MC.objects.all())

    data = []
    for metric in metrics:
        latest = metric.data.latest()
        data.append({'metric': metric, 'latest': latest})
    return render(request, 'index.html', {'data': data})
