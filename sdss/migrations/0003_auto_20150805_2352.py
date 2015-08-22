# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sdss', '0002_auto_20150805_2305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='version_of',
            field=models.ForeignKey(blank=True, to='sdss.Song', null=True),
        ),
    ]
