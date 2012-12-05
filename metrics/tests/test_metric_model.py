from django.test import TestCase

from metrics.models import Metric


class MetricModelTestCase(TestCase):
    def test_should_have_name_field(self):
        fields = Metric._meta.get_all_field_names()
        self.assertIn("name", fields)

    def test_should_have_url_field(self):
        fields = Metric._meta.get_all_field_names()
        self.assertIn("url", fields)
