from django.test import TestCase


class IndexViewTestCase(TestCase):
    def test_should_have_metrics_on_context(self):
        response = self.client.get("/")
        self.assertIn("object_list", response.context)
