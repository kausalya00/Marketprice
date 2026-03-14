from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    # All users are just "user" — no seller role
    pass
