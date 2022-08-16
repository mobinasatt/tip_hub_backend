from django.urls import path
from . import views


app_name = 'video'
urlpatterns = [
    path('all/', views.AllVideoView.as_view(), name='all'),
    path('<slug:slug>/', views.VideoDetailView.as_view(), name='detail'),
]
