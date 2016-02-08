# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('petition', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='petition',
            name='comment',
            field=models.CharField(default=datetime.datetime(2016, 2, 8, 11, 21, 46, 914369, tzinfo=utc), max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='petition',
            name='verdict',
            field=models.CharField(default=datetime.datetime(2016, 2, 8, 11, 21, 50, 10059, tzinfo=utc), max_length=100),
            preserve_default=False,
        ),
    ]
