from django.shortcuts import render
from django.views import generic
from django.http import JsonResponse
from .custom_json import CustomJSONEncoder

from .models import Track

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

def get_songs(request):
    #songs = Song.objects.all().values('id', 'title', 'writers', 'originally_by', 'is_single')
    tracks = Track.objects.filter(release__album_type=1) \
      .values('song__id', 'song__title', 'song__is_single',
              'song__originally_by', 'release__release_date',
              'release__title', 'duration')
    return JsonResponse(list(tracks), encoder=CustomJSONEncoder, safe=False)

# def get_releases(request):
#     releases = list(Release.objects.all().values('id','title','release_date'))
#     for release in releases:
#         release['tracklist'] = list(Track.objects.filter(release__id=release['id'])\
#           .values('track_number','song__title','get_duration_seconds'))
#     return JsonResponse(releases, safe=False)
