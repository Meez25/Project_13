from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    Profile model extending the built-in User model to include extra
    information.

    Attributes:
        user: A one-to-one relationship with the User model.
        favorite_city: A character field that holds the user's favorite city.
        This field is optional.

    Methods:
        __str__: Returns the username of the associated user.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        """
        Return the username of the associated User object.

        Returns:
            str: The username of the associated User object.
        """
        return self.user.username
