from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.db import models
from .models import (Profile, Tasks)
from django.forms import ModelForm
import datetime
from datetime import date
from django.utils.safestring import mark_safe
from django import forms
from django.core.files.images import get_image_dimensions

class Registration(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(Registration, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user


class EditProfile(ModelForm):

    class Meta:
        model = Profile

        fields = (
            'bio', 'jobtitle', 'dob', 'profilepic'
        )
        labels = {
            'bio': 'Your Bio',
            'jobtitle': 'Your Job Title',
            'dob': 'Date of Birth',
            'profilepic': 'Profile Picture'
        }

    def save(self, commit=True):
        profile = super(EditProfile, self).save(commit=False)
        profile.bio = self.cleaned_data['bio']
        profile.jobtitle = self.cleaned_data['jobtitle']
        profile.dob = self.cleaned_data['dob']
        profile.profilepic = self.cleaned_data['profilepic']

        today = date.today()
        profile.age = today.year - profile.dob.year - ((today.month, today.day) < (profile.dob.month, profile.dob.day))

        if commit:
            profile.save()

        return profile


# class CreateTask(ModelForm):
#
#     class Meta:
#         model = Tasks
#
#         fields = ['profile', 'task', 'type']
#         labels = {
#             'task': 'Your Task',
#             'type': 'Either To Do or Completed!',
#         }
#
#     def save(self, commit=True):
#         task = super(CreateTask, self).save(commit=False)
#         tasks = Tasks.objects.create(profile=task.profile, task=task.task, type=task.type)
#
#         if commit:
#             tasks.save()
#
#         return tasks
