# Generated by Django 2.2.10 on 2020-04-21 20:29

from django.db import migrations
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('maps', '0004_mapstyle'),
    ]

    operations = [
        migrations.AddField(
            model_name='mappage',
            name='map_styles',
            field=modelcluster.fields.ParentalManyToManyField(blank=True, to='maps.MapStyle'),
        ),
    ]