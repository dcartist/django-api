from rest_framework import serializers, generics
from rest_framework.pagination import PageNumberPagination
from .models import *



class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')

class RemixLevelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RemixLevel
        fields = ('id', 'level')

class ArtistSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Artist
        fields = ('id', 'name', 'alternative_name')

class SongSerializer(serializers.HyperlinkedModelSerializer):
    artist = ArtistSerializer(read_only=True)
    category = CategorySerializer(read_only=True)
    remix_level = RemixLevelSerializer(read_only=True)
    class Meta:
        model = Song
        fields = ('id', 'title', 'lyrics', 'artist', "category", "remix_level")

class SongDetail(generics.RetrieveAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

class CategoryDetail(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

