# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20150522_0732'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='hour',
            field=models.DateTimeField(max_length=9999),
            preserve_default=True,
        ),
    ]
