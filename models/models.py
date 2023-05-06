from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class PhoneNumbers(models.Model):
    number = models.IntegerField(default=0)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)