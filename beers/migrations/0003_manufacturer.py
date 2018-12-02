# Generated by Django 2.1.3 on 2018-12-02 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beers', '0002_auto_20181117_0128'),
    ]

    operations = [
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('url', models.URLField(blank=True)),
                ('location', models.CharField(blank=True, max_length=50)),
                ('logo_url', models.URLField(blank=True)),
                ('facebook_url', models.URLField(blank=True)),
                ('twitter_handle', models.CharField(blank=True, max_length=50)),
                ('instagram_handle', models.CharField(blank=True, max_length=50)),
            ],
        ),
    ]
