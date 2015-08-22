# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sdss', '0006_auto_20150808_2352'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='bpm',
        ),
        migrations.RemoveField(
            model_name='song',
            name='duration',
        ),
        migrations.RemoveField(
            model_name='song',
            name='key',
        ),
        migrations.RemoveField(
            model_name='song',
            name='mode',
        ),
        migrations.RemoveField(
            model_name='song',
            name='version_info',
        ),
        migrations.RemoveField(
            model_name='song',
            name='version_of',
        ),
        migrations.AddField(
            model_name='track',
            name='bpm',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='track',
            name='duration',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='track',
            name='version_info',
            field=models.CharField(default=b'', max_length=80, blank=True),
        ),
    ]
