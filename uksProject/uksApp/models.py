from unittest.util import _MAX_LENGTH

from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=100)
    key = models.CharField(unique=True, max_length=10)
    owner = models.ForeignKey(to=User, null=False, related_name="owner")
    contributors = models.ManyToManyField(to=User, blank=True, related_name="contributors")
    description = models.TextField()
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('project')
