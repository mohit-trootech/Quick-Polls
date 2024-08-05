# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from accounts.constants import USER_PROFILE_MEDIA_URL


class User(AbstractUser):
    profile = models.ImageField(upload_to=USER_PROFILE_MEDIA_URL, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    address = models.CharField(max_length=50, null=True, blank=True)
    phone = PhoneNumberField(region="IN", blank=True, null=True)  # type: ignore

    def __str__(self):
        return self.username
