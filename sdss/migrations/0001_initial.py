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
                ('album_type', models.PositiveSmallIntegerField(default=0, choices=[(1, b'LP'), (2, b'EP'), (3, b'single'), (4, b'compilation'), (5, b'live'), (0, b'other')])),
                ('release_date', models.DateField()),
            ],
            options={
                'ordering': ['release_date'],
            },
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=80)),
                ('is_single', models.BooleanField(default=False, verbose_name=b'Single?')),
                ('originally_by', models.CharField(default=b'', help_text=b'Name of the original band or musician if this song is a cover, otherwise blank', max_length=80, blank=True)),
                ('writers', models.ManyToManyField(help_text=b'Select none if this is a cover song', to='sdss.BandMember', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('track_number', models.PositiveSmallIntegerField()),
                ('version_info', models.CharField(default=b'', help_text=b'This is the text in parentheses after a song name', max_length=80, blank=True)),
                ('duration', models.DurationField(default=0)),
                ('release', models.ForeignKey(to='sdss.Release')),
                ('song', models.ForeignKey(to='sdss.Song')),
            ],
            options={
                'ordering': ['track_number'],
            },
        ),
        migrations.AddField(
            model_name='release',
            name='tracks',
            field=models.ManyToManyField(to='sdss.Song', through='sdss.Track'),
        ),
    ]
