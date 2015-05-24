# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_activitie_point'),
    ]

    operations = [
        migrations.AddField(
            model_name='userspage',
            name='background',
            field=models.CharField(default=b'#396b83', max_length=9999),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userspage',
            name='text',
            field=models.CharField(default=b'#555555', max_length=9999),
            preserve_default=True,
        ),
    ]
