from django.db import models

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    email=models.EmailField(max_length=100)
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    dob=models.DateField(null=True, blank=True)
    img=models.ImageField(default="default.jpg",upload_to="profile_pics")

    def __str__(self):
        return f'{self.user.username} Profile'
