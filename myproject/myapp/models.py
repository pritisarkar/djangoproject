# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class Employee(models.Model):
    username = models.CharField(max_length = 100)
    password = models.CharField()
    def __str__(self):
        return self.name
    
class customer(models.Model):
    username = models.CharField(max_length = 100)
    password = models.CharField()
    def __str__(self):
        return self.name