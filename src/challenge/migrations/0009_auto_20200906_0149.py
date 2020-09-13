# Generated by Django 3.0.5 on 2020-09-06 00:49

import challenge.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenge', '0008_file_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='upload',
            field=models.FileField(upload_to=challenge.models.get_file_name),
        ),
        migrations.AlterField(
            model_name='file',
            name='url',
            field=models.URLField(max_length=255),
        ),
    ]