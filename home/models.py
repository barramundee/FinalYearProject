from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
import datetime
from datetime import date


# Create your models here.


class Profile(models.Model):
    created = models.DateTimeField(auto_now_add=True, editable=False)

    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, default='')
    bio = models.CharField(max_length=100, default='')
    jobtitle = models.CharField(max_length=100, default='')
    dob = models.DateField(("Date"), default=datetime.date.today)
    age = models.IntegerField(default=0)
    completedtasks = models.IntegerField(default=0)
    profilepic = models.ImageField(upload_to='profile_image', blank=True)

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

    def create_profile(sender, **kwargs):
        if kwargs['created']:
            profile = Profile.objects.create(user=kwargs['instance'], name=kwargs['instance'],bio="This is your Bio.",
                                             jobtitle="This is your Job Title.", dob=date.today(),
                                             profilepic='profile_image/default.png')

    def calculate_age(self, dob):
        today = date.today()
        self.age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))

    post_save.connect(create_profile, sender=User)


class Tasks(models.Model):
    created = models.DateTimeField(auto_now_add=True, editable=False)

    profile = models.CharField(max_length=255, default='')
    task = models.CharField(max_length=255, default='')
    type = models.CharField(max_length=100, default='', help_text='todo, completed')
    points = models.IntegerField(default=0, help_text='Story Points')
    votes = models.IntegerField(default=0, help_text='')

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'
        ordering = ['-points', '-votes']


class NewsFeed(models.Model):
    created = models.DateTimeField(auto_now_add=True, editable=False)

    profile = models.CharField(max_length=255, default='')
    post = models.CharField(max_length=255, default='')

    class Meta:
        verbose_name = 'News Feed'
        verbose_name_plural = 'News Feed'
        ordering = ['-created']


