# Django packeges
from django.shortcuts import render
from django.views import View
# Local apps
from video.models import Video


class HomeView(View):
    def get(self, request):
        video = Video.objects.all()

        context = {
            'video': video
        }
        return render(request, 'home/index.html', context)
