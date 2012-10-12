from django.http import HttpResponse
from taggit.models import Tag
from django.utils.datastructures import MultiValueDictKeyError
from django.utils import simplejson

def taggit_autocomplete_list(request):
    try:
        q_list = request.GET['term'].split(",")
        q = q_list[len(q_list) - 1]
        tags = ["%s" % x for x in Tag.objects.filter(name__istartswith=q).values_list('name', flat=True)]
    except MultiValueDictKeyError,e:
        print e
        tags = []
        pass
    return HttpResponse(simplejson.dumps(tags))
