# Django packages
from django.views import generic
# Local apps
from .models import Video


class ListVideo(generic.ListView):
    model = Video


class VideoDetail(generic.DetailView):
    model = Video
