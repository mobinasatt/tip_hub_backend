# Django packages
from django.shortcuts import render, get_object_or_404
from django.views import View
# Local apps
from .models import Video


class AllVideoView(View):
    def get(self, request):
        videos = Video.objects.all().order_by('-created')

        context = {'videos': videos}
        return render(request, 'video/all_videos.html', context)


class VideoDetailView(View):
    def get(self, request, slug):
        video = get_object_or_404(Video, slug=slug)
        video.video_view()

        context = {
            'video': video
        }
        return render(request, 'video/video_detail.html', context)
