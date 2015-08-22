from django.shortcuts import render
from django.views import generic

from .models import Release

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
