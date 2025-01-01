from django.db import models
from users.models import User

class Group(models.Model):
    name = models.CharField(max_length=255)
    members = models.ManyToManyField(
        User,
        related_name='custom_groups',  # Change related_name to avoid conflict
        blank=True,
    )