from django.conf.urls.defaults import *
import os

DOC_ROOT = os.path.abspath('taggit_live/static_taggit_live')

urlpatterns = patterns('',
    (r'^static_taggit_live/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': DOC_ROOT}),
    url(r'^taggit_autocomplete_list/$', 'taggit_live.views.taggit_autocomplete_list', name='taggit_autocomplete_list')                  
)
