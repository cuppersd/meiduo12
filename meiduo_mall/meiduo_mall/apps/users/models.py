from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    mobile = models.CharField(max_length=11, unique=True, verbose_name="mobile number")

    class Meta:
        db_table = 'tb_users'

    def __str__(self):
        return self.username