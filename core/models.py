from typing import Iterable
from django.db import models

# Create your models here.
class Gallery(models.Model):
    image = models.ImageField(upload_to="gallery/")
    alt = models.CharField(null=True, blank=True)
    upload_date = models.DateTimeField(auto_now_add=True)