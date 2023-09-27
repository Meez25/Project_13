from django.test import TestCase
from lettings.models import Address, Letting
import pytest


class TestAddressModel(TestCase):

    @pytest.mark.django_db  # Marking it for database access
    def setup_method(self, method):
        self.address = Address.objects.create(
            number=1234,
            street="Main Street",
            city="Anytown",
            state="CA",
            zip_code=12345,
            country_iso_code="USA",
        )

    @pytest.mark.django_db
    def test_str_representation(self):
        assert str(self.address) == '1234 Main Street'


class TestLettingModel(TestCase):

    @pytest.mark.django_db
    def setup_method(self, method):
        test_address = Address.objects.create(
            number=1234,
            street="Main Street",
            city="Anytown",
            state="CA",
            zip_code=12345,
            country_iso_code="USA",
        )
        self.letting = Letting.objects.create(
            title="title",
            address=test_address
        )

    @pytest.mark.django_db
    def test_str_representation(self):
        assert str(self.letting) == "title"
