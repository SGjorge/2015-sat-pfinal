# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activitie',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=9999)),
                ('price', models.CharField(max_length=9999)),
                ('date', models.CharField(max_length=9999)),
                ('startHour', models.CharField(max_length=9999)),
                ('typ', models.CharField(max_length=9999)),
                ('timeToLong', models.CharField(max_length=9999)),
                ('Long', models.CharField(max_length=9999)),
                ('Url', models.CharField(max_length=9999)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hour', models.TextField(max_length=9999)),
                ('date', models.CharField(max_length=9999)),
                ('activities', models.ForeignKey(to='app.Activitie')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UsersPage',
            fields=[
                ('user', models.CharField(max_length=9999, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=9999)),
                ('activities', models.ManyToManyField(to='app.Activitie')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='publication',
            name='user',
            field=models.ForeignKey(to='app.UsersPage'),
            preserve_default=True,
        ),
    ]
