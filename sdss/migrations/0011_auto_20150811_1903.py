# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sdss', '0010_auto_20150811_1802'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='originally_by',
            field=models.CharField(default=b'', help_text=b'Name of the original band or musician if this song is a cover, otherwise blank', max_length=80, blank=True),
        ),
        migrations.AlterField(
            model_name='song',
            name='writers',
            field=models.ManyToManyField(help_text=b'Select none if this is a cover song', to='sdss.BandMember', blank=True),
        ),
    ]
