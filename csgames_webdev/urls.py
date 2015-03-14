from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^spookyducky/', include('spookyducky.urls', namespace = 'spookyducky')),
    url(r'^admin/', include(admin.site.urls)),
)
