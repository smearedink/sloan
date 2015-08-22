# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sdss', '0008_auto_20150810_0912'),
    ]

    operations = [
        migrations.AlterField(
            model_name='release',
            name='album_type',
            field=models.PositiveSmallIntegerField(default=0, choices=[(1, b'LP'), (2, b'EP'), (3, b'single'), (4, b'compilation'), (5, b'live'), (0, b'other')]),
        ),
    ]
