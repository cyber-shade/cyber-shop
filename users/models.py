from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _



class User(AbstractUser):
    first_name = models.CharField()
    last_name = models.CharField()
    phone_number = models.IntegerField(null=True, blank=True)
    username = models.CharField(unique=True)
    password = models.CharField()
    email = models.EmailField(unique=True)
    address = models.TextField()
    birthdate = models.DateField(null=True, blank=True)
    profile_image = models.ImageField(upload_to="users/", null=True, blank=True)    
    
    def __str__(self):
        return self.username
