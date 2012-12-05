from django.test import TestCase

from metrics.models import Metric

import mock


class MetricModelTestCase(TestCase):
    def test_should_have_name_field(self):
        fields = Metric._meta.get_all_field_names()
        self.assertIn("name", fields)

    def test_should_have_url_field(self):
        fields = Metric._meta.get_all_field_names()
        self.assertIn("url", fields)

    def test_fetch_should_add_data(self):
        metric = Metric.objects.create(
            name="issues",
            url="https://api.github.com/repos/globocom/tsuru"
        )
        with mock.patch("requests.get") as get:
            get.return_value = mock.Mock(json={"open_issues": 105})
            metric.fetch()
        data = metric.data_set.all()[0]
        self.assertEqual(105, data.count)
