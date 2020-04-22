# Generated by Django 2.2.10 on 2020-04-22 08:19

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maps', '0008_auto_20200422_0940'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mappage',
            name='lat_long',
        ),
        migrations.AddField(
            model_name='mappage',
            name='long_lat',
            field=models.CharField(blank=True, help_text='Comma separated long/lat. (Ex. Torino is 7.676111, 45.079167)', max_length=36, null=True, validators=[django.core.validators.RegexValidator(code='invalid_long_lat', message='Lat Long must be a comma-separated numeric long and lat', regex='^(\\-?\\d+(\\.\\d+)?),\\s*(\\-?\\d+(\\.\\d+)?)$')]),
        ),
    ]