# Generated by Django 3.0.3 on 2020-06-13 07:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('small_business', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='businessdata',
            old_name='allowedArea',
            new_name='allowed_area',
        ),
    ]
