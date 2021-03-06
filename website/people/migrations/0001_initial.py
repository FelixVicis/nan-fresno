# Generated by Django 2.0.7 on 2018-07-17 22:57

import datetime
from django.db import migrations, models
import people.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('lastName', models.CharField(max_length=200)),
                ('firstName', models.CharField(blank=True, max_length=200, null=True)),
                ('city', models.CharField(blank=True, max_length=200, null=True)),
                ('state', models.CharField(blank=True, max_length=200, null=True)),
                ('county', models.CharField(blank=True, max_length=200, null=True)),
                ('country', models.CharField(blank=True, max_length=200, null=True)),
                ('circumstance', models.TextField()),
                ('age', models.CharField(blank=True, max_length=4, null=True)),
                ('sex', models.CharField(blank=True, max_length=20, null=True)),
                ('race', models.CharField(blank=True, max_length=100, null=True)),
                ('eye_color', models.CharField(blank=True, max_length=200, null=True)),
                ('hair_color', models.CharField(blank=True, max_length=200, null=True)),
                ('weight', models.CharField(blank=True, max_length=200, null=True)),
                ('height', models.CharField(blank=True, max_length=200, null=True)),
                ('photo', models.ImageField(upload_to=people.models.upload_location)),
                ('created_at', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
            options={
                'verbose_name_plural': 'Missing People',
            },
        ),
    ]
