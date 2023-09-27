from django.test import TestCase
from django.urls import reverse
from lettings.models import Letting, Address


class LettingListViewTest(TestCase):
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/lettings/')
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        url = reverse('lettings:index')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'lettings/index.html')

    def test_view_contains_some_text(self):
        url = reverse('lettings:index')
        response = self.client.get(url)
        self.assertContains(response, 'Lettings')


class LettingDetailViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        address = Address.objects.create(
            number=1234,
            street="Main Street",
            city="Anytown",
            state="CA",
            zip_code=12345,
            country_iso_code="USA"
        )
        cls.letting = Letting.objects.create(
            title="Test Title",
            address=address,
        )

    def test_view_url_exists_at_desired_location(self):
        url = reverse('lettings:letting', args=[self.letting.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        url = reverse('lettings:letting', args=[self.letting.id])
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'lettings/letting.html')

    def test_view_contains_title(self):
        url = reverse('lettings:letting', args=[self.letting.id])
        response = self.client.get(url)
        self.assertContains(response, 'Test Title')

    def test_view_contains_address(self):
        url = reverse('lettings:letting', args=[self.letting.id])
        response = self.client.get(url)
        self.assertContains(response, '1234 Main Street')
