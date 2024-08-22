from django.db import models
from django.core.validators import MaxValueValidator

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class RemixLevel(models.Model):
    level = models.IntegerField(default=0, null=False, blank=False, validators=[MaxValueValidator(5)]) 
    def __int__(self):
        return self.level
    def __str__(self):
        return str(self.level)
    
class Artist(models.Model):
    name = models.CharField(max_length=100)
    alternative_name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name

class Song(models.Model):
    title = models.CharField(max_length=200)
    lyrics = models.TextField(null=True, blank=True)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='songs')
    categories = models.ManyToManyField(Category, related_name='songs')
    remix_level = models.ForeignKey(RemixLevel, on_delete=models.CASCADE, related_name='songs', default=0)

    def __str__(self):
        return self.title
    








    
