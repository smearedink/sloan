# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sdss', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='duration',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
