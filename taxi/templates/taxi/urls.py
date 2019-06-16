from django.urls import path
from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf.urls.static import static
from django.conf import settings
from .views import *


from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('import-disks/',TextTxtCreate.as_view(),name='texttxt_create_url'),
    path('import-musics/',music_multiple_get,name='multiple_music_get_create_url'),
    path('import-musics-post/',music_multiple_post,name='multiple_music_post_create_url'),
    path('',albums_list,name='albums_list_url'),
    path('reports/',list_report,name='list_report_url'),
    path('report1/',report1,name='report1'),
    path('report2/',report2,name='report2'),
    path('queries/',list_query,name='list_query_url'),
    path('query/',query_list,name='query_list_url'),
    path('query1/',query1,name='query1'),
    path('query2/',query2,name='query2'),
    path('query3/',query3,name='query3'),
    path('query4/',query4,name='query4'),
    path('accounts/profile/', profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='music/login.html'), name='login'),
    path('register/', register, name='register'),
    path('logout/', auth_views.LogoutView.as_view(template_name='music/logout.html'), name='logout'),
    path('like/',like_group,name='like_group'),
    path('groups/',groups_list,name='groups_list_url'),
    path('group/create/',GroupCreate.as_view(),name='group_create_url'),
    path('group/<str:slug>/', GroupDetail.as_view(), name='group_detail_url'),
    path('group/<str:slug>/update/', GroupUpdate.as_view(), name='group_update_url'),
    path('group/<str:slug>/delete/', GroupDelete.as_view(), name='group_delete_url'),
    path('artists/',artists_list,name='artists_list_url'),
    path('artist/create/',ArtistCreate.as_view(),name='artist_create_url'),
    path('artist/<str:slug>/', ArtistDetail.as_view(), name='artist_detail_url'),
    path('artist/<str:slug>/update/', ArtistUpdate.as_view(), name='artist_update_url'),
    path('artist/<str:slug>/delete/', ArtistDelete.as_view(), name='artist_delete_url'),
    #path('albums/',albums_list,name='albums_list_url'),
    path('album/create/',AlbumCreate.as_view(),name='album_create_url'),
    path('album/<str:slug>/', AlbumDetail.as_view(), name='album_detail_url'),
    path('album/<str:slug>/update/', AlbumUpdate.as_view(), name='album_update_url'),
    path('album/<str:slug>/delete/', AlbumDelete.as_view(), name='album_delete_url'),
    path('songs/',songs_list,name='songs_list_url'),
    path('song/create/',SongCreate.as_view(),name='song_create_url'),
    path('song/<str:slug>/', SongDetail.as_view(), name='song_detail_url'),
    path('song/<str:slug>/update/', SongUpdate.as_view(), name='song_update_url'),
    path('song/<str:slug>/delete/', SongDelete.as_view(), name='song_delete_url'),
]
