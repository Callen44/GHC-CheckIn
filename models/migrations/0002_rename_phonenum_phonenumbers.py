# Generated by Django 4.2.1 on 2023-05-06 18:21

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('models', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PhoneNum',
            new_name='PhoneNumbers',
        ),
    ]
