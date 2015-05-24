# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20150522_1153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='date',
            field=models.DateTimeField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='publication',
            name='hour',
            field=models.DateTimeField(),
            preserve_default=True,
        ),
    ]
