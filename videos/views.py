from wsgiref.util import request_uri
from django.shortcuts import render
from videos.models import Video

# Create your views here.
def index_video(request):
    videos = Video.objects.all()
    context = {
        'videos' : videos,
    }
    return render(request, 'video.html', context)