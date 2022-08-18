# Django packages
from django.shortcuts import render
from django.views import View
# Local apps
from video.models import Video


class HomeView(View):
    def get(self, request, *args, **kwargs):
        video = Video.objects.all().order_by('-updated')[:6]
        most_visit_video = Video.objects.all().order_by('-views')[:3]

        context = {
            'video': video,
            'most_visit': most_visit_video,
        }
        return render(request, 'home/index.html', context)
