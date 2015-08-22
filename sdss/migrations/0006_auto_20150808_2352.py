# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sdss', '0005_remove_track_release_version'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='track',
            options={'ordering': ['track_number']},
        ),
    ]
