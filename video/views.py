# Django packages
from django.shortcuts import render, get_object_or_404
from django.views import generic
# Local apps
from .models import Video, Comment


class ListVideo(generic.ListView):
    model = Video
    context_object_name = 'videos'


def detail_video(request, pk, slug):
    video = get_object_or_404(Video, id=pk, slug=slug)
    video.video_view()

    if request.method == 'POST':
        parent_id = request.POST.get('parent_id')
        body = request.POST.get('body')
        if parent_id:
            Comment.objects.create(body=body, video=video, user=request.user, parent_id=parent_id)
        else:
            Comment.objects.create(body=body, video=video, user=request.user)

    context = {
        'video': video
    }
    return render(request, 'video/video_detail.html', context)


def search(request):
    q = request.GET.get("q")
    videos = Video.objects.filter(title__icontains=q)

    context = {'videos': videos}
    return render(request, 'video/video_list.html', context)
