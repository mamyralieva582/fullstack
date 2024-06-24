from django.urls import path

from .views import PlaylistListView, PlaylistDetail

urlpatterns = [
    path('playlists', PlaylistListView.as_view()),
    path('playlist/<slug:slug>/', PlaylistDetail.as_view())
]
