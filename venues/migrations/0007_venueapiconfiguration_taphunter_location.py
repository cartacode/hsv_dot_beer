# Generated by Django 2.1.5 on 2019-02-12 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venues', '0006_auto_20190205_2208'),
    ]

    operations = [
        migrations.AddField(
            model_name='venueapiconfiguration',
            name='taphunter_location',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
