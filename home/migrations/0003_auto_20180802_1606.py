# Generated by Django 2.0.7 on 2018-08-02 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20180802_1532'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='profile',
            field=models.CharField(default='', max_length=255),
        ),
    ]