from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    
	url(r'^sent/$', 'location.views.sent', name='sent'),
    url(r'^view/$', 'location.views.viewLocation', name='viewLocation'),
    url(r'^json/(?P<id_location>\d+)/$', 'location.views.viewLocationJSON', name='viewLocationJSON'),
    url(r'^json/$', 'location.views.viewAllJSON', name='viewAllJSON'),
    url(r'^video/$', 'location.views.downloadVideo', name='downloadVideo'),
    url(r'^video/download$', 'location.views.formVideo', name='formVideo'),

)	