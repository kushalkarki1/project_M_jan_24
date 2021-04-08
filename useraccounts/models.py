from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    contact = models.CharField(max_length=255, null=True, blank=True)
    avtar = models.ImageField(upload_to="avtar/", null=True, blank=True)
    bank_name = models.CharField(max_length=255, null=True, blank=True)
    bank_branch = models.CharField(max_length=255, null=True, blank=True)
    cheque_number = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return str(self.user)