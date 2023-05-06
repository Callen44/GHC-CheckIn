from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class PhoneNumber(models.Model):
    number = models.IntegerField(default=0)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

class Children(models.Model):
    name = models.CharField(max_length=100)
    special_notes = models.CharField(max_length=100)
    parent = models.ForeignKey(User, on_delete=models.CASCADE)