# Generated by Django 2.1.5 on 2019-02-03 14:21

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0006_auto_20190203_1719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 5, 14, 21, 43, 828836, tzinfo=utc)),
        ),
    ]
