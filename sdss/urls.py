from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^plot_stuff', views.plot_stuff, name='plot_stuff'),
    url(r'^api/get_tracks', views.get_tracks, name='get_tracks'),
    url(r'^api/get_LPs', views.get_LPs, name='get_LPs'),
]
