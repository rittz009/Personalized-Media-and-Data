from __future__ import unicode_literals

from django.db import models
from django.urls import reverse

import shelve

class Movie(models.Model):
    Name=models.CharField(max_length=300)
    Year=models.CharField(max_length=5)
    Plot=models.CharField(max_length=1500)
    Genre=models.CharField(max_length=250)
    Imdb_rating=models.FloatField(default=0.0)
    Plot_outline=models.CharField(max_length=1000,default=None)
    Director=models.CharField(max_length=50,default=None)
    Poster=models.FileField()
    Path=models.CharField(max_length=100)
    Watched=models.BooleanField(default=False)
    trailer=models.CharField(max_length=150,default=None,null=True,blank=True)

    def __str__(self):
        return self.Name



class UpdateList(models.Model):
    title = models.CharField(max_length = 200)
    text = models.TextField()


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('movie_page')
