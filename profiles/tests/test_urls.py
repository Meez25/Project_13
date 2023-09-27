from django.test import SimpleTestCase
from django.urls import reverse, resolve
from profiles.views import index, profile


class TestUrls(SimpleTestCase):
    def test_index_url_is_resolved(self):
        url = reverse('profiles:index')
        self.assertEqual(resolve(url).func, index)

    def test_detail_url_is_resolved(self):
        username = "Test"
        url = reverse("profiles:profile", kwargs={"username": username})
        self.assertEqual(resolve(url).func, profile)
