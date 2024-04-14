


from django.db import models
from django.contrib.auth.models import AbstractUser

class Doctor(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    Name=models.CharField(max_length=100 , default=None)
    specialization = models.CharField(max_length=100,default=None)
    experience_years = models.PositiveIntegerField(default=None)
    location = models.CharField(max_length=100,default=None)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default=None)
    date_of_birth = models.DateField(default=None)
    email = models.EmailField(unique=True,default=None)
    phone_number = models.CharField(max_length=15, blank=True, null=True,default=None)
    profile_picture = models.ImageField(upload_to='doctor_profiles/', blank=True, null=True)
    biography = models.TextField(blank=True)

    def __str__(self):
        return self.Name

from django.db import models

class Patient(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    address = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
