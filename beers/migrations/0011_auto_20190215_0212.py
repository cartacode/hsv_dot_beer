# Generated by Django 2.1.7 on 2019-02-15 02:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beers', '0010_auto_20190213_0231'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='beer',
            name='untappd_id',
        ),
        migrations.AddField(
            model_name='beer',
            name='untappd_url',
            field=models.URLField(blank=True, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='manufacturer',
            name='untappd_url',
            field=models.URLField(blank=True, null=True, unique=True),
        ),
    ]
