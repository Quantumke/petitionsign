# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('petition', '0002_auto_20160208_1121'),
    ]

    operations = [
        migrations.AddField(
            model_name='petition',
            name='route',
            field=models.CharField(max_length=100, default=datetime.datetime(2016, 2, 8, 11, 32, 6, 790043, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
