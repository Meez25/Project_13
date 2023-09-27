from django.test import TestCase
from django.contrib.auth.models import User
from profiles.models import Profile
import pytest


class TestProfilModel(TestCase):

    @pytest.mark.django_db
    def setup_method(self, method):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.profile = Profile.objects.create(
            user=self.user,
            favorite_city="Test City",
        )

    @pytest.mark.django_db
    def test_str_representation(self):
        self.assertEqual(str(self.profile), 'testuser')
