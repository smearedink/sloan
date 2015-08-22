# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sdss', '0009_auto_20150811_1655'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='track',
            name='bpm',
        ),
        migrations.AddField(
            model_name='song',
            name='originally_by',
            field=models.CharField(default=b'', help_text=b'Name of the original band if this song is a cover', max_length=80, blank=True),
        ),
        migrations.AlterField(
            model_name='track',
            name='version_info',
            field=models.CharField(default=b'', help_text=b'This is the text in parentheses after a song name', max_length=80, blank=True),
        ),
    ]
