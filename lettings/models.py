from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator


class Address(models.Model):
    """Represents an address with its various components."""
    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(
        validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(
        max_length=3, validators=[MinLengthValidator(3)])

    def __str__(self):
        """Returns a string representation of the address."""
        return f'{self.number} {self.street}'

    class Meta:
        """Metadata for the Address model."""
        verbose_name_plural = "Address"


class Letting(models.Model):
    """Represents a letting with a title and associated address."""
    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        """Returns the title of the letting as its string representation."""
        return self.title
