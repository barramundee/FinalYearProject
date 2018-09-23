# Generated by Django 2.0.7 on 2018-08-02 14:30

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('bio', models.CharField(default='', max_length=100)),
                ('jobtitle', models.CharField(default='', max_length=100)),
                ('dob', models.DateField(default=datetime.date.today, verbose_name='Date')),
                ('age', models.IntegerField(default=0)),
                ('profilepic', models.ImageField(blank=True, upload_to='profile_image')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Profile',
                'verbose_name_plural': 'Profiles',
            },
        ),
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('task', models.CharField(default='', max_length=255)),
                ('type', models.CharField(default='', help_text='todo, completed', max_length=100)),
                ('points', models.IntegerField(default=0, help_text='Story Points')),
                ('profile_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='task', to='home.Profile')),
            ],
            options={
                'verbose_name': 'Task',
                'verbose_name_plural': 'Tasks',
            },
        ),
    ]
