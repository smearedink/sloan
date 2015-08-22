# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sdss', '0007_auto_20150810_0855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='track',
            name='duration',
            field=models.DurationField(default=0),
        ),
    ]
