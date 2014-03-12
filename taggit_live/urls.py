from django.conf.urls import patterns, url
import os

urlpatterns = patterns('',
    url(r'^taggit_autocomplete_list/$', 'taggit_live.views.taggit_autocomplete_list', name='taggit_autocomplete_list')
)
