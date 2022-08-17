from django.urls import path
from . import views


app_name = 'video'
urlpatterns = [
    path('all/', views.ListVideo.as_view(), name='all'),
    path('<int:pk>/<slug:slug>/', views.VideoDetail.as_view(), name='detail'),
]
