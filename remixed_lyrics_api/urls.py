from django.urls import path
from . import views

urlpatterns = [
    path('', views.CategoryList.as_view(), name='CategoryList'),
    path('artists/', views.ArtistList.as_view(), name='ArtistList'),
    path('songs/', views.SongList.as_view(), name='SongList'),
    path('categories/', views.CategoryList.as_view(), name='CategoryList'),
    # path('artists/<int:pk>/', views.ArtistDetail.as_view(), name='ArtistDetail'),
    # path('songs/<int:pk>/', views.SongDetail.as_view(), name='SongDetail'),

]