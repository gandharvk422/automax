from email.policy import default
from django.db import models
from django.contrib.auth.models import User

from localflavor.in_.models import INStateField
from localflavor.in_.forms import INZipCodeField as INZipCodeFormField

from .utils import user_directory_path

class INZipCodeField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('max_length', 6)
        super().__init__(*args, **kwargs)
    
    def formfield(self, **kwargs):
        defaults = {'form_class': INZipCodeFormField}
        defaults.update(kwargs)
        return super().formfield(**defaults)

class Location(models.Model):
    address_1 = models.CharField(max_length=128, blank=True)
    address_2 = models.CharField(max_length=128, blank=True)
    city = models.CharField(max_length=64)
    state = INStateField(default="MH")
    zip_code = INZipCodeField(blank=True)

    def __str__(self):
        return f"{self.address_1}, {self.city}, {self.state}"

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to=user_directory_path, null=True)
    bio = models.CharField(max_length=140, blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    location = models.OneToOneField(
        Location,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='profile'
    )

    def __str__(self):
        return f"{self.user.username}'s Profile"