from django.db import models

from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    username = models.CharField(max_length=50, unique=True, error_messages={'unique': "O usuario cadastrado já existe."})
    password = models.CharField(max_length=8)
    email = models.EmailField(max_length=254, unique=True, error_messages={'unique': "O email cadastrado já existe."})


    USERNAME_FIELD = 'username'
