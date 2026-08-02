from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import User, CandidateProfile, EmployerProfile


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):

    if not created:
        return

    if instance.role == User.Role.CANDIDATE:
        CandidateProfile.objects.create(user=instance)

    elif instance.role == User.Role.EMPLOYER:
        EmployerProfile.objects.create(
            user=instance,
            company_name=f"{instance.username}'s Company"
        )