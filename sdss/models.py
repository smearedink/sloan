from django.db import models
from django.core import checks
from django.core.exceptions import ValidationError
from datetime import timedelta

class BandMember(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    instrument = models.CharField(max_length=20)
    birth_date = models.DateField()
    def __unicode__(self):
        return self.first_name
    def get_full_name(self):
        return self.first_name + " " + self.last_name
    get_full_name.short_description = "Name"
    get_full_name.admin_order_field = 'last_name'

class Song(models.Model):
    title = models.CharField(max_length=80)
    writers = models.ManyToManyField(BandMember, blank=True,\
      help_text="Select none if this is a cover song")
    is_single = models.BooleanField(default=False, verbose_name="Single?")
    originally_by = models.CharField(max_length=80, blank=True, default="",\
      help_text="Name of the original band or musician if this song is a cover, otherwise blank")
    def __unicode__(self):
        return self.title
    ## for some reason this breaks the ability to add songs, at least in the
    ## release view
    #def clean(self):
    #    # Check that a cover song has no Sloan band members as writers
    #    if self.writers.count() and self.originally_by:
    #        raise ValidationError('Song is a cover but has Sloan band members entered as writers.')

class Track(models.Model):
    """
    An intermediate model for the many-to-many relation between Releases
    and Songs.
    """
    song = models.ForeignKey('Song')
    release = models.ForeignKey('Release')
    track_number = models.PositiveSmallIntegerField()
    def __unicode__(self):
        if self.version_info:
            return "%s track %d: %s (%s)" % (self.release.title, self.track_number,
                                             self.song.title, self.version_info)
        else:
            return "%s track %d: %s" % (self.release.title, self.track_number,
                                        self.song.title)
    class Meta:
        ordering = ['track_number']

    # version_of = models.ForeignKey('self', null=True, blank=True)
    # text in brackets after song name:
    version_info = models.CharField(max_length=80, blank=True, default="",\
      help_text="This is the text in parentheses after a song name")
    duration = models.DurationField(default=0)
    #bpm = models.PositiveSmallIntegerField(default=0)

    # KEY_CHOICES = (
    #     (0, 'C'),
    #     (1, 'C sharp'),
    #     (2, 'D'),
    #     (3, 'E flat'),
    #     (4, 'E'),
    #     (5, 'F'),
    #     (6, 'F sharp'),
    #     (7, 'G'),
    #     (8, 'A flat'),
    #     (9, 'A'),
    #     (10, 'B flat'),
    #     (11, 'B'),
    # )
    # key = models.PositiveSmallIntegerField(choices=KEY_CHOICES,
    #                                        null=True, blank=True)
    # MODE_CHOICES = (
    #     (0, 'minor'),
    #     (1, 'major'),
    # )
    # mode = models.PositiveSmallIntegerField(choices=MODE_CHOICES,
    #                                         null=True, blank=True)

    #def get_formatted_duration(self):
    #    minutes = self.duration / 60
    #    seconds = self.duration % 60
    #    return "%d:%02d" % (minutes, seconds)
    #get_formatted_duration.short_description = 'Length'
    #get_formatted_duration.admin_order_field = 'duration'

class Release(models.Model):
    title = models.CharField(max_length=80)
    tracks = models.ManyToManyField(Song, through='Track')
    TYPE_CHOICES = (
        (1, 'LP'),
        (2, 'EP'),
        (3, 'single'),
        (4, 'compilation'),
        (5, 'live'),
        (0, 'other'),
    )
    album_type = models.PositiveSmallIntegerField(choices=TYPE_CHOICES,
                                                  default=0)
    release_date = models.DateField()
    def __unicode__(self):
        return self.title

    def get_ntracks(self):
        return self.tracks.count()
    get_ntracks.short_description = "Number of tracks"

    def get_duration(self):
        return sum([t.duration for t in Track.objects.filter(release=self)], timedelta())
    get_duration.short_description = "Length"

    def get_track_starts(self):
        durations = [t.duration for t in Track.objects.filter(release=self)]
        return [sum(durations[:ii], timedelta()) for ii in range(self.get_ntracks())]

    class Meta:
        ordering = ['release_date']

    """
    def get_formatted_duration(self):
        nsec = self.get_duration()
        minutes = nsec / 60
        seconds = nsec % 60
        return "%d:%02d" % (minutes, seconds)
    get_formatted_duration.short_description = 'Length'
    """
