# Generated by Django 3.0.3 on 2020-06-20 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('small_business', '0002_auto_20200613_1651'),
    ]

    operations = [
        migrations.AddField(
            model_name='businessdata',
            name='start_time',
            field=models.DateTimeField(null=True),
        ),
    ]
