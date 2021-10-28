# Generated by Django 3.2.8 on 2021-10-28 05:02

import datetime
import django.contrib.gis.db.models.fields
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('geometry', django.contrib.gis.db.models.fields.PointField(geography=True, srid=4326)),
                ('description', models.TextField()),
                ('date_added', models.DateTimeField(default=datetime.datetime.today)),
            ],
        ),
    ]
