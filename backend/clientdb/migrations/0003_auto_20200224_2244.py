# Generated by Django 3.0.3 on 2020-02-24 14:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientdb', '0002_profile_is_active'),
    ]

    operations = [
        migrations.RenameModel('Profile', 'Client'),
    ]