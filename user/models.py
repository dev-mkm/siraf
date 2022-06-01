from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.exceptions import ValidationError
from file.models import file

def phonenumber(value):
    if len(value) != 11 or value.startswith("09"):
        raise ValidationError('Invalid Number')

class User(AbstractUser):
    phoneNumber = models.CharField(max_length=11 ,validators=[phonenumber])
    birthDate = models.DateField()
    gender = models.CharField(max_length=1, choices=(
        ('M', 'Male'),
        ('F', 'Female'),))
    bio = models.TextField()
    status = models.BooleanField()

class Favorites(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.ForeignKey(file, on_delete=models.CASCADE)