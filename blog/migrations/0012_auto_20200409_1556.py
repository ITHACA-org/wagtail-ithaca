# Generated by Django 2.2.10 on 2020-04-09 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20200311_1744'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpage',
            name='intro',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]