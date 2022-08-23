from tkinter import CASCADE
from django.db import models
import datetime
from django.contrib.auth.models import User



# Create your models here.


class Todo(models.Model):
    title = models.CharField(max_length=100)
    date_time = datetime.datetime.now()
    person = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
   
    def __str__(self):
        return self.title


