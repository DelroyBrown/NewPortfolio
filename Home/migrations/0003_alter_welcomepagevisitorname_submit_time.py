# Generated by Django 4.1.7 on 2023-03-06 11:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0002_welcomepagevisitorname_submit_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='welcomepagevisitorname',
            name='submit_time',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
