# Generated by Django 4.2.1 on 2023-05-06 18:33

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('models', '0003_children'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PhoneNumbers',
            new_name='PhoneNumber',
        ),
    ]
