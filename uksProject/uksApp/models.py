from django.core.validators import MaxValueValidator, MinValueValidator

from django.db import models
from django.contrib.auth.models import User

SILVER = "default"
BLUE = "primary"
GREEN = "success"
LIGHT_BLUE = "info"
YELLOW = "warning"
RED = "danger"
MARKER_CHOICES = (
    (SILVER, 'silver'),
    (BLUE, 'blue'),
    (GREEN, 'green'),
    (LIGHT_BLUE, 'light blue'),
    (YELLOW, 'yellow'),
    (RED, 'red')
)

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=100)
    key = models.CharField(unique=True, max_length=10)
    owner = models.ForeignKey(to=User, null=False, related_name="owner")
    contributors = models.ManyToManyField(to=User, blank=True, related_name="contributors")
    description = models.TextField()
    
    def __str__(self):
        return self.name
    
    
class Status(models.Model):
    name = models.CharField(max_length=20)
    key = models.CharField(unique=True, max_length=10)
    marker = models.CharField(max_length=15, choices=MARKER_CHOICES, default=SILVER)

    def __str__(self):
        return self.name
    

class Milestone(models.Model):
    name = models.CharField(max_length=20)
    key = models.CharField(unique=True, max_length=10)
    marker = models.CharField(max_length=15, choices=MARKER_CHOICES, default=SILVER)

    def __str__(self):
        return self.name
    
    
class IssueType(models.Model):
    name = models.CharField(max_length=20)
    key = models.CharField(unique=True, max_length=10)
    marker = models.CharField(max_length=15, choices=MARKER_CHOICES, default=SILVER)

    def __str__(self):
        return self.name
    
    
class Priority(models.Model):
    name = models.CharField(max_length=20)
    key = models.CharField(unique=True, max_length=10)
    marker = models.CharField(max_length=15, choices=MARKER_CHOICES, default=SILVER)

    def __str__(self):
        return self.name
    
    
    
class Issue(models.Model):
    title = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    finishDate = models.DateField(null=True)
    project = models.ForeignKey(to=Project, null=False)
    createdBy = models.ForeignKey(to=User, null=False, related_name='createdBy')
    assignedTo = models.ForeignKey(to=User, null=True, blank=True, related_name='assignedTo')
    status = models.ForeignKey(to=Status, null=False)
    milestone = models.ForeignKey(to=Milestone, null=True, blank=True)
    label = models.ForeignKey(to=IssueType, null=False, verbose_name='Issue type')
    priority = models.ForeignKey(to=Priority, null=True, blank=True)
    description = models.TextField()
    timeSpent = models.PositiveIntegerField(default=0, validators=[
        MinValueValidator(0)
    ])
    donePercentage = models.PositiveIntegerField(validators=[
        MaxValueValidator(100),
        MinValueValidator(0)
    ])


    def __str__(self):
        return self.title

    
    
class Commit(models.Model):
    hashcode = models.CharField(max_length=64, primary_key=True)
    message = models.TextField()
    dateTime = models.DateTimeField()
    project = models.ForeignKey(to=Project, null=False)
    issue = models.ManyToManyField(to=Issue, blank=True, related_name='commits')
    user = models.TextField(null=False)

    def __str__(self):
        return self.hashcode


class Comment(models.Model):
    message = models.TextField()
    dateTime = models.DateTimeField()
    author = models.ForeignKey(to=User, null=False)
    issue = models.ForeignKey(to=Issue, null=False)


    def __str__(self):
        return self.message
    

