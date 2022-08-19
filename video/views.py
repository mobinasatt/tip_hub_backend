# Django packages
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.http import JsonResponse
# Local apps
from .models import Video, Comment, Category, Like


def video_list(request):
    videos = Video.objects.all()
    # Pagination
    page_number = request.GET.get('page')
    paginator = Paginator(videos, 6)
    object_list = paginator.get_page(page_number)

    context = {'videos': object_list}
    return render(request, 'video/video_list.html', context)


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
    if request.user.is_authenticated:
        if request.user.user_likes.filter(video_id=pk, user_id=request.user.id).exists():
            context['is_liked'] = True
        else:
            context['is_liked'] = False
    else:
        return redirect('accounts:login')

    return render(request, 'video/video_detail.html', context)


def search(request):
    q = request.GET.get("q")
    videos = Video.objects.filter(title__icontains=q)
    # Pagination
    page_number = request.GET.get('page')
    paginator = Paginator(videos, 6)
    objects_list = paginator.get_page(page_number)

    context = {'videos': objects_list}
    return render(request, 'video/video_list.html', context)


def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    videos = category.cvideos.all()
    # Pagination
    page_number = request.GET.get('page')
    paginator = Paginator(videos, 6)
    objects_list = paginator.get_page(page_number)

    context = {'videos': objects_list}
    return render(request, 'video/video_list.html', context)


def like(request, slug, pk):
    try:
        like = Like.objects.get(video__slug=slug, user_id=request.user.id)
        like.delete()
        return JsonResponse({'response': 'unliked'})
    except:
        Like.objects.create(video_id=pk, user_id=request.user.id)
        return JsonResponse({'response': 'liked'})
