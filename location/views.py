from django.template.context import RequestContext

from django.shortcuts import render, render_to_response



def index(request):

	title = ".::TIGO::."

	return render_to_response('index.html', {'title': title}, context_instance=RequestContext(request))



def sent(request):

	pass
