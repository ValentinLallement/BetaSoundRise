# Generated by Django 5.0.6 on 2024-06-23 04:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beats', '0014_beats_views_alter_beats_release_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='beats',
            name='score',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='beats',
            name='release_date',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]