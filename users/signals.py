from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile


# User profile


@receiver(post_save, sender=User)  # When a user is save send this
def create_profile(sender, instance, created, **kwargs):
    # if the user is created, create a profile for each user created
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)  # When a user is save send this
def save_profile(sender, instance, **kwargs):
    # Save profile
    instance.profile.save()
