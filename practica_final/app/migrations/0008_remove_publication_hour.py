# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20150522_1452'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='publication',
            name='hour',
        ),
    ]
