from django.template.context import RequestContext

from django.shortcuts import render, render_to_response

from django.http import HttpResponse, HttpResponseRedirect

from location.forms import PositionForm

from location.models import Position



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
