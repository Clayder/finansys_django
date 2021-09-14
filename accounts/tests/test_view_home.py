from django.test import TestCase
from accounts.forms import SubscriptionForm


class AccountTest(TestCase):
    def setUp(self):
        self.resp = self.client.get("/accounts/")

    def test_get(self):
        """GET /accounts/ must return status code 200"""
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        """Must use accounts/account_form.html"""
        self.assertTemplateUsed(self.resp, 'accounts/account_form.html')

    def test_html(self):
        """Html must contain input tags"""
        self.assertContains(self.resp, '<form')
        self.assertContains(self.resp, '<input', 6)
        self.assertContains(self.resp, 'type="submit"')

    def test_csrf(self):
        """Html must contain csrf"""
        self.assertContains(self.resp, 'csrfmiddlewaretoken')

    def test_has_form(self):
        """Context must have subscription form """
        form = self.resp.context['form']
        self.assertIsInstance(form, SubscriptionForm)

    def test_form_has_fields(self):
        """Form must have 4 fields"""
        form = self.resp.context['form']
        self.assertSequenceEqual(['name', 'balance', 'bank', 'due_day', 'closing_day'], list(form.fields))
