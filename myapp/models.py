from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(default='',blank=True)
    is_recruiter = models.BooleanField(default=False)
