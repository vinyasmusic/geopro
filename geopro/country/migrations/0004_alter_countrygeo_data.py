# Generated by Django 3.2.13 on 2022-07-05 16:59

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('country', '0003_remove_countrygeo_is_removed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='countrygeo',
            name='data',
            field=django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326),
        ),
    ]