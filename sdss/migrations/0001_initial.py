# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BandMember',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('instrument', models.CharField(max_length=20)),
                ('birth_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Release',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=80)),
                ('album_type', models.CharField(max_length=20)),
                ('release_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=80)),
                ('version_info', models.CharField(default=b'', max_length=80, blank=True)),
                ('is_single', models.BooleanField(default=False)),
                ('duration', models.FloatField(default=0)),
                ('bpm', models.PositiveSmallIntegerField(default=0)),
                ('key', models.PositiveSmallIntegerField(blank=True, null=True, choices=[(0, b'C'), (1, b'C sharp'), (2, b'D'), (3, b'E flat'), (4, b'E'), (5, b'F'), (6, b'F sharp'), (7, b'G'), (8, b'A flat'), (9, b'A'), (10, b'B flat'), (11, b'B')])),
                ('mode', models.PositiveSmallIntegerField(blank=True, null=True, choices=[(0, b'minor'), (1, b'major')])),
                ('version_of', models.ForeignKey(to='sdss.Song', null=True)),
                ('writers', models.ManyToManyField(to='sdss.BandMember', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('release_version', models.CharField(default=b'canonical', max_length=80)),
                ('track_number', models.PositiveSmallIntegerField()),
                ('release', models.ForeignKey(to='sdss.Release')),
                ('song', models.ForeignKey(to='sdss.Song')),
            ],
        ),
        migrations.AddField(
            model_name='release',
            name='tracks',
            field=models.ManyToManyField(to='sdss.Song', through='sdss.Track'),
        ),
    ]
