# Generated by Django 3.2.4 on 2021-06-29 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aperitivos', '0002_video_creation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='slug',
            field=models.SlugField(max_length=32),
        ),
    ]
