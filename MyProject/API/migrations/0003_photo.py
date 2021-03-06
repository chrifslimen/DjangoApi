# Generated by Django 2.2.13 on 2020-06-27 01:32

import API.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0002_compte'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to=API.models.uploadPath)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('syndrom', models.CharField(max_length=100)),
            ],
        ),
    ]
