from django.db import models 
from django.contrib.auth import get_user_model

User = get_user_model()

class Playlist(models.Model):
    author = models.ForeignKey(User, related_name='playlist', on_delete=models.CASCADE, verbose_name='автор')
    name = models.CharField(max_length=25)
    description = models.TextField()
    song_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
