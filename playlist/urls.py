from django.urls import path

from .views import PlaylistListView

urlpatterns = [
    path('playlists', PlaylistListView.as_view(), name='playlist-list')
]