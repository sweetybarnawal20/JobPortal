from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):

    class Role(models.TextChoices):
        CANDIDATE = "CANDIDATE", "Candidate"
        EMPLOYER = "EMPLOYER", "Employer"

    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.CANDIDATE,
    )
    
class CandidateProfile(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
    )

    phone = models.CharField(
        max_length=20,
        blank=True,
    )

    address = models.CharField(
        max_length=200,
        blank=True,
    )

    bio = models.TextField(
        blank=True,
    )

    skills = models.TextField(
        blank=True,
    )

    education = models.TextField(
        blank=True,
    )

    experience = models.TextField(
        blank=True,
    )

    resume = models.FileField(
        upload_to="resumes/",
        blank=True,
        null=True,
    )

    profile_picture = models.ImageField(
        upload_to="profile_pictures/",
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.user.username    