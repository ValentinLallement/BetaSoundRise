# Generated by Django 5.0.6 on 2024-06-23 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beats', '0016_alter_beats_release_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beats',
            name='audio_file',
            field=models.FileField(upload_to='audio/beats/mp3'),
        ),
    ]