from django.test import SimpleTestCase
from django.urls import reverse, resolve
from lettings.views import index, letting


class TestUrls(SimpleTestCase):
    def test_index_url_is_resolved(self):
        url = reverse('lettings:index')
        self.assertEqual(resolve(url).func, index)

    def test_detail_url_is_resolved(self):
        letting_id = 1
        url = reverse("lettings:letting", kwargs={"letting_id": letting_id})
        self.assertEqual(resolve(url).func, letting)
