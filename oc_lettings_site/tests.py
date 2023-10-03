# tests.py in your Django app

from django.test import TestCase


class CustomErrorPagesTests(TestCase):

    def test_custom_404_page(self):
        # Trigger a 404 error by visiting a non-existent URL
        response = self.client.get('/non-existent-url/')
        # Check if the response has a 404 status code
        self.assertEqual(response.status_code, 404)
        # Check if the custom 404.html template is used
        self.assertTemplateUsed(response, '404.html')

    def test_custom_500_page(self):
        # You have to manually trigger the 500 error
        try:
            response = self.client.get('/sentry-debug/')
        except ZeroDivisionError:
            pass

        self.assertTemplateUsed(response, '500.html')

