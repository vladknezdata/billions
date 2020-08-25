from django.urls import path
from . import views

app_name='references'

urlpatterns = [
    path('reference/<slug:slug>/', views.detail_view, name='detail_view'),
    path('references/', views.list_view, name='list_view'),
    path('references/<slug:tag_slug>/', views.list_view, name='list_view_by_tag'),
    path('episode/<int:episode_number>/', views.list_view, name='list_view_by_episode'),
    path('seasons/', views.season_list_view, name='seasons_list'),
    path('seasons/<int:season_number>/', views.season_detail_view, name='season_view'),
    path('characters/', views.character_list_view, name='characters'),
    path('character/', views.character_detail_view, name='character')
]