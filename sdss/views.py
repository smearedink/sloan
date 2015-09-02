from django.shortcuts import render
from django.views import generic
from django.http import JsonResponse
from .custom_json import CustomJSONEncoder

from .models import Track, Release, BandMember

class IndexView(generic.ListView):
    template_name = 'sdss/index.html'
    context_object_name = 'release_list'

    def get_queryset(self):
        # """
        # Return the last five published questions (not including those set to be
        # published in the future).
        # """
        # return Question.objects.filter(
        #     pub_date__lte=timezone.now()
        # ).order_by('-pub_date')[:5]
        return Release.objects.filter(album_type=1)

def get_tracks(request):
    #songs = Song.objects.all().values('id', 'title', 'writers', 'originally_by', 'is_single')
    tracks = list(
      Track.objects.filter(release__album_type=1) \
        .values('song__id', 'song__title', 'song__is_single',
                'song__originally_by',
                'release__id', 'release__title', 'release__release_date',
                'duration', 'track_number', 'id')
    )
    for ii in range(len(tracks)):
        tracks[ii]['writers'] = list(BandMember.objects \
          .filter(song__id=tracks[ii]['song__id']) \
          .values_list('first_name', flat=True))

    return JsonResponse(tracks, encoder=CustomJSONEncoder, safe=False)

def get_LPs(request):
    albums = Release.objects.filter(album_type=1) \
      .values('id', 'release_date', 'title')

    return JsonResponse(list(albums), encoder=CustomJSONEncoder, safe=False)

def plot_stuff(request):
    return render(request, 'sdss/plot_stuff.html')

# def get_releases(request):
#     releases = list(Release.objects.all().values('id','title','release_date'))
#     for release in releases:
#         release['tracklist'] = list(Track.objects.filter(release__id=release['id'])\
#           .values('track_number','song__title','get_duration_seconds'))
#     return JsonResponse(releases, safe=False)
