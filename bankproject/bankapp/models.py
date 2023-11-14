
from django.db import models

class Register(models.Model):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=100)
    confirm_password = models.CharField(max_length=100)

    def __str__(self):
        return self.username

class Registration(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField()
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.TextField()
    district = models.CharField(max_length=15)
    branch = models.CharField(max_length=15)
    accountType = models.CharField(max_length=50)
    materials_provide = models.BooleanField(max_length=255)

    def __str__(self):
        return self.name










