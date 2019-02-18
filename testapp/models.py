from __future__ import unicode_literals

from django.conf import settings
from django.db import models
from django.utils import timezone

class Benutzer(models.Model):
 name = models.CharField(max_length=20)
 vorname = models.CharField(max_length=30)
 username = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

# Create your models here.
