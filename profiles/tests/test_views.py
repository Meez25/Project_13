from django.test import TestCase
from django.urls import reverse
from profiles.models import Profile
from django.contrib.auth.models import User


class ProfileListViewTest(TestCase):
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/profiles/')
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        url = reverse('profiles:index')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'profiles/index.html')

    def test_view_contains_some_text(self):
        url = reverse('lettings:index')
        response = self.client.get(url)
        self.assertContains(response, 'Profiles')


class ProfileDetailViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(
            username='testuser',
            password='testpass123',
            email="email@email.com",
        )
        cls.profile = Profile.objects.create(
            user=cls.user,
            favorite_city="Test City",
        )

    def test_view_url_exists_at_desired_location(self):
        url = reverse('profiles:profile', args=[self.profile])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        url = reverse('profiles:profile', args=[self.profile])
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'profiles/profile.html')

    def test_view_contains_firstname(self):
        url = reverse('profiles:profile', args=[self.profile])
        response = self.client.get(url)
        self.assertContains(response, 'First name')

    def test_view_contains_lastname(self):
        url = reverse('profiles:profile', args=[self.profile])
        response = self.client.get(url)
        self.assertContains(response, 'Last name')

    def test_view_contains_email(self):
        url = reverse('profiles:profile', args=[self.profile])
        response = self.client.get(url)
        self.assertContains(response, 'email@email.com')

    def test_view_contains_favorite_city(self):
        url = reverse('profiles:profile', args=[self.profile])
        response = self.client.get(url)
        self.assertContains(response, 'Test City')
