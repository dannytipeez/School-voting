from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class CustomUser(AbstractUser):
    school = models.CharField(max_length=300)

    def __str__(self):
        return self.username