from django.db import models
from django.contrib.auth.models import  AbstractUser
import uuid


# Create your models here.
AGE_CHOICES = (
    ('ALL', 'ALL'),
    ('Kids', 'Kids')
)

MOVIE_CHOICES = (
    ('seasonal', 'Seasonal'),
    ('single', 'Single'),
)
class CustomUser(AbstractUser):
    profiles = models.ManyToManyField('Profile', blank=True)
class Profile(models.Model):
    name = models.CharField(max_length=1000)
    age_limit = models.CharField(max_length=10, choices=AGE_CHOICES, default='ALL')
    uid = models.UUIDField(default=uuid.uuid4)

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=1000)
    description = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    uuid = models.UUIDField(default=uuid.uuid4)
    type = models.CharField(choices=MOVIE_CHOICES, max_length=10)
    Video = models.ManyToManyField('Video')
    image = models.ImageField(upload_to='covers')
    age_limit = models.CharField(max_length=10, choices=AGE_CHOICES)

    def __str__(self):
        return self.title

class Video(models.Model):
    title = models.CharField(max_length=1000)
    file = models.FileField(upload_to='movies')

    def __str__(self):
        return self.title