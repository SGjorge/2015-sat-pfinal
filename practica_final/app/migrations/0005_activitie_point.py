# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20150522_0739'),
    ]

    operations = [
        migrations.AddField(
            model_name='activitie',
            name='point',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
