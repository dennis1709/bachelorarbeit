from __future__ import unicode_literals

from django.conf import settings
from django.db import models

class Benutzer(models.Model):
    name = models.CharField(max_length=20)
    vorname = models.CharField(max_length=30)
    userid = models.CharField(max_length=10)
    
    def publish(self):
	self.save()

    def __str__(self):
	return self.userid

# Create your models here.
