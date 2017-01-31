from django.conf.urls import url
from .views import TaggitAutocompleteView

urlpatterns = [
    url(r'^taggit_autocomplete_list/$',
        TaggitAutocompleteView.as_view(),
        name='taggit_autocomplete_list')
]
