# Generated by Django 3.2.13 on 2022-06-10 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('country', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='countrygeo',
            name='iso_code',
            field=models.CharField(max_length=4, unique=True),
        ),
    ]