from rest_framework import serializers
from .models import *



class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'category')
        # read_only_fields=True

class ArtistSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Artist
        fields = ('id', 'name', 'alternative_name')
        # read_only_fields=True

class SongSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Song
        fields = ('id', 'title', 'lyrics', 'artist', 'categories')
        # read_only_fields=True

