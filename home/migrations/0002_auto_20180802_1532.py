# Generated by Django 2.0.7 on 2018-08-02 14:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tasks',
            old_name='profile_id',
            new_name='profile',
        ),
    ]
