from django.test import TestCase

from metrics.models import Data


class DataModelTestCase(TestCase):
    def test_should_have_count_field(self):
        fields = Data._meta.get_all_field_names()
        self.assertIn("count", fields)

    def test_should_have_date_field(self):
        fields = Data._meta.get_all_field_names()
        self.assertIn("date", fields)
