# Generated by Django 2.2 on 2020-11-28 13:26

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20201127_1647'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 28, 13, 26, 48, 348567, tzinfo=utc)),
        ),
    ]
