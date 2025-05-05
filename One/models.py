from django.db import models

from django.contrib.auth.models import User
from django.template.context_processors import request


class Track(models.Model):
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    genre = models.CharField(max_length=255,null=True,blank=True)
    cover_image = models.URLField(null=True,blank=True)
    audio_url = models.URLField()
    album = models.ForeignKey('Album',on_delete=models.CASCADE,related_name='tracks',null=True,blank=True)


    def __str__(self):
        return f"{self.title} - {self.artist}"

class Album(models.Model):
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    cover_image = models.URLField(null=True,blank=True)

    def __str__(self):
        return f"{self.title} - {self.artist}"

class Favorite(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    track = models.ForeignKey(Track,on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user','track')

    def __str__(self):
        return f"{self.user.username} - {self.track.title}"




class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    last_played_tracks = models.ManyToManyField(Track,related_name='last_played',blank=True)

    def __str__(self):
        return f"{self.user.username}"


