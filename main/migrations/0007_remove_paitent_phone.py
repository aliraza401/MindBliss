# Generated by Django 3.1.6 on 2021-02-10 18:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20210207_1707'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paitent',
            name='phone',
        ),
    ]
