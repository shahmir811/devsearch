from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from django.contrib.auth.models import User
from .models import Profile

# @receiver(post_save, sender=Profile)
def createProfile(sender, instance, created, **kwargs):
  user = instance  # instance will be the sender which is the User in this case (line 55)
  if created == True:  # It will be true when the user is first created else it will be false
      Profile.objects.create(
          user=user,
          name=user.first_name,
          email=user.email,
          username=user.username
      )

def deleteProfile(sender, instance, **kwargs):
    user = instance.user
    user.delete()

post_save.connect(createProfile, sender=User)
post_delete.connect(deleteProfile, sender=Profile)
