# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sdss', '0003_auto_20150805_2352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='release',
            name='album_type',
            field=models.PositiveSmallIntegerField(default=0, choices=[(1, b'LP'), (2, b'EP'), (3, b'single'), (4, b'compilation'), (0, b'other')]),
        ),
        migrations.AlterField(
            model_name='song',
            name='is_single',
            field=models.BooleanField(default=False, verbose_name=b'Single?'),
        ),
    ]
