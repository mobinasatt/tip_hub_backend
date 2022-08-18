from django.urls import path
from . import views


app_name = 'video'
urlpatterns = [
    # Videos
    path('all/', views.video_list, name='all'),
    path('<int:pk>/<slug:slug>/', views.detail_video, name='detail'),
    # Search
    path('search/', views.search, name='search-videos'),
]
