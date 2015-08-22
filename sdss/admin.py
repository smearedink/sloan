from django.contrib import admin
from django.db import models
from django.forms import CheckboxSelectMultiple

from .models import Song, BandMember, Release, Track

class TrackInline(admin.TabularInline):
    model = Track
    extra = 0

class TrackAdmin(admin.ModelAdmin):
    list_display = ['song', 'release', 'track_number', 'duration']

class SongAdmin(admin.ModelAdmin):
    inlines = (TrackInline,)

    """
    fieldsets = [
        (None,                    {'fields': ['title', 'writers', 'is_single']}),
        #('Version information',   {'fields': ['version_of', 'version_info'],
        #                           'classes': ['collapse']}),
        #('Technical information', {'fields': ['duration', 'bpm', 'key', 'mode'],
        #                           'classes': ['collapse']}),
    ]
    """

    fields = ['title', 'writers', 'originally_by', 'is_single']

    #formfield_overrides = {
    #    models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    #}

    #list_display = ('title', 'get_formatted_duration', 'is_single',
    #                'get_writers_string')
    list_display = ('title', 'is_single', 'get_writers_string')

    def get_writers_string(self, obj):
        out_str = ""
        if obj.writers.count():
            for w in obj.writers.get_queryset():
                out_str += w.first_name + ", "
            out_str = out_str[:-2]
        elif obj.originally_by:
            out_str = "cover: %s" % obj.originally_by
        return out_str
    get_writers_string.short_description = 'Writers'

class ReleaseAdmin(admin.ModelAdmin):
    inlines = (TrackInline,)

    list_display = ('title', 'album_type', 'get_ntracks', 'get_duration',#'get_formatted_duration',
                    'release_date')
    #fields = ['title', 'tracks', 'album_type', 'release_date']

class BandMemberAdmin(admin.ModelAdmin):
    list_display = ('get_full_name', 'instrument', 'birth_date')

admin.site.register(Song, SongAdmin)
admin.site.register(BandMember, BandMemberAdmin)
admin.site.register(Release, ReleaseAdmin)
admin.site.register(Track, TrackAdmin)
