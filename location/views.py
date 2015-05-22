import json, pafy
from django.template.context import RequestContext
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from .forms import PositionForm, VideoDown
from .models import Position

def index(request):
    title = ".::GEOLOCATION::."
    return render_to_response('index.html', {'title': title}, context_instance=RequestContext(request))

def sent(request):
    title = ".::GEOLOCATION::."
    ipClient = request.META['HTTP_X_FORWARDED_FOR']
    if request.method=='POST':
        form = PositionForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        default_data = {'latitude': '1', 'longitude':'2', 'phone': ipClient, 'count': '0' }
        form = PositionForm(default_data)
    return render_to_response('form.html', {'form':form, 'title':title}, context_instance=RequestContext(request))

def viewLocation(request):
    title = ".::GEOLOCATION::."
    pos = Position.objects.all()
    return render_to_response('view.html', {'title':title, 'pos': pos}, context_instance=RequestContext(request))

def viewLocationJSON(request, id_location):
    title = ".::GEOLOCATION::."
    # pos = Position.objects.get(id=id_location)
    pos = Position.objects.all()
    for item in pos:
        data = {
            'latitude': item.latitude,
            'longitude': item.longitude,
            'phone': item.phone,
            'count': item.count,
        }
    json_data = json.dumps(data)
    return HttpResponse(json_data, content_type='application/json')
    # json.loads(string_json)

def downloadVideo(request):
    if request.method == 'POST':
        link = request.POST['link']
        video = pafy.new(link)
        data =  {
            'title': video.title,
            'author': video.author,
            'videoId': video.videoid,
            'duration': video.duration,
            'keywords': video.keywords,
        }
        json_data = json.dumps(data)
        return HttpResponse(json_data, content_type='application/json')
    else:
        form = VideoDown()
    return render_to_response('formvideo.html', {'form': form}, context_instance=RequestContext(request))

def formVideo(request):
    if request.method == 'POST':
        link = request.POST['link']
        path = request.POST['path']
        # video = pafy.new(link)
        # filepath = path
        # fileVideo = video.getbest()
        # fileVideo.download()
        return render_to_response('index.html', {'link': link, 'path': path}, context_instance=RequestContext(request))
    else:
        form = VideoDown()
    return render_to_response('formvideo.html', {'form': form}, context_instance=RequestContext(request))