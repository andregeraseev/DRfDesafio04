from django.db import models

from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    username = models.SlugField(max_length=40, unique=True, error_messages={'unique': "O usuario cadastrado já existe."})
    password = models.CharField(max_length=30)
    email = models.EmailField(max_length=30, unique=True, error_messages={'unique': "O email cadastrado já existe."})


    USERNAME_FIELD = 'username'


