# Generated by Django 3.2.7 on 2021-10-16 22:03

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='image'),
        ),
    ]
