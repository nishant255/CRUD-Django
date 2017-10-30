from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Person(models.Model):

    userName = models.CharField(max_length=50,default='')
    firstName = models.CharField(max_length=100,default='')
    lastName = models.CharField(max_length=100,default='')
    email = models.EmailField(max_length=50,default='')

    def __str__(self):
        return self.userName






