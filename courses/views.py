from django.shortcuts import render, get_object_or_404, redirect
from .models import Course, Video, Comment

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'courses/course_list.html', {'courses': courses})

def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    return render(request, 'courses/course_detail.html', {'course': course})

def video_detail(request, pk):
    video = get_object_or_404(Video, pk=pk)

    if request.method == "POST":
        # Обработка добавления комментария
        author = request.POST.get('author')
        content = request.POST.get('content')
        if author and content:
            Comment.objects.create(
                video=video,
                author=author,
                content=content
            )
        return redirect('video_detail', pk=pk)  # Перенаправление на текущую страницу видео

    # Отображение видео и комментариев
    comments = video.comments.all()
    return render(request, 'courses/video_detail.html', {'video': video, 'comments': comments})
