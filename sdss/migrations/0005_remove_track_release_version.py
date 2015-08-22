# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sdss', '0004_auto_20150808_2255'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='track',
            name='release_version',
        ),
    ]
