from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.CategoryList.as_view(), name='CategoryList'),
    path('artists/', views.ArtistList.as_view(), name='ArtistList'),
    path('songs/', views.SongList.as_view(), name='SongList'),
    path('categories/', views.CategoryList.as_view(), name='CategoryList'),
    path('remixlevels/', views.RemixLevelList.as_view(), name='RemixLevelList'),
    path('artists/<int:pk>/', views.ArtistDetail.as_view(), name='ArtistDetail'),
    path('songs/<int:pk>/', views.SongDetail.as_view(), name='SongDetail'),
    path('categories/<int:pk>/', views.CategoryDetail.as_view(), name='CategoryDetail'),
    path('category/<int:pk>/', views.CategoryDetail.as_view(), name='CategoryDetail'),
    re_path(r'^(?P<path>.*)$', views.CategoryList.as_view(), name='CategoryList'),
  
]