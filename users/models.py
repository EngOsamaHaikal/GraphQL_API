from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
active_roles=(
    ("user", "user"),
    ("manager", "manager")
)


class ExtendUser(AbstractUser):

    email = models.EmailField(blank=False, max_length=255, verbose_name="email")
    role = models.CharField(max_length=120, choices=active_roles, default="user")

    USERNAME_FIELD = "username"
    EMAIL_FIELD = "email"


