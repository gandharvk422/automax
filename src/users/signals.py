from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Profile, Location

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        # Only create Profile here (no Location)
        Profile.objects.create(user=instance)

@receiver(post_save, sender=Profile)
def set_profile_location(sender, instance, created, **kwargs):
    if created:
        # Create ONE default location and link it
        profile_location = Location.objects.create(
            address_1="3rd Flr, 16, Manu Mansion",
            address_2="Shahid Bhagat Singh Marg, Fort",
            city="Mumbai",  # Default values
            state="MH",
            zip_code="400001"
        )
        instance.location = profile_location
        instance.save()

@receiver(post_delete, sender=Profile)
def delete_profile_location(sender, instance, *args, **kwargs):
    if instance.location:
        instance.location.delete()