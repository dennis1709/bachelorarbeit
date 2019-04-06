from __future__ import unicode_literals

from django.conf import settings
from django.db import models

class Benutzer(models.Model):
    name = models.CharField(max_length=20)
    vorname = models.CharField(max_length=30)
    alter = models.IntegerField()
    
# Create your models here.
