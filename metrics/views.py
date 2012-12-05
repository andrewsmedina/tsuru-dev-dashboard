from django.views.generic import ListView

from metrics.models import Metric


class Index(ListView):
    model = Metric
