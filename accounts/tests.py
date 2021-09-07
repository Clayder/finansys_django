from django.test import TestCase


class AccountTest(TestCase):
    def test_get(self):
        """GET /accounts/ must return status code 200"""
        response = self.client.get("/accounts/")
        self.assertEqual(200, response.status_code)
