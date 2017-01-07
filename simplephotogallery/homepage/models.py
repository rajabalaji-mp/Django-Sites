from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Gallery(models.Model):
    photo_caption=models.CharField(max_length=150)
    photo_description=models.CharField(max_length=1000)
    photo_file=models.FileField()
    def __str__(self):
        return self.photo_caption