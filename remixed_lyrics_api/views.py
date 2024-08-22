from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *

# Create your views here.



class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ArtistList(generics.ListAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

class SongList(generics.ListAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer


