from django.test import TestCase


class AccountTest(TestCase):
    def setUp(self):
        self.resp = self.client.get("/accounts/")

    def test_get(self):
        """GET /accounts/ must return status code 200"""
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        """Must use accounts/account_form.html"""
        self.assertTemplateUsed(self.resp, 'accounts/account_form.html')
