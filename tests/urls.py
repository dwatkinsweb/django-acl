from django.conf.urls import patterns, url
from django.conf.urls import include

urlpatterns = patterns('', url(r'', include('cms.urls')))
