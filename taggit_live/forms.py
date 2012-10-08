from django import forms
from django.conf import settings
from django.utils.safestring import mark_safe
from taggit.forms import TagField
from taggit.utils import edit_string_for_tags
from django.core.urlresolvers import reverse

class TaggitLiveWidget(forms.TextInput):
    class Media:
        css = {'all': ('/static_taggit_live/css/taggit_live.css',
                       )}
        js = ('/static_taggit_live/js/taggit_live.js',
              )
    def render(self, name, value, attrs=None):
        if value is not None and not isinstance(value, basestring):
            value = edit_string_for_tags([o.tag for o in value.select_related("tag")])
        rendered = super(TaggitLiveWidget, self).render(name, value, attrs)
        js = u'<script type="text/javascript">jQuery(function() { $("#%s").taggit_live(); });</script>' % (attrs['id'])
        return rendered + mark_safe(js)

class LiveTagField(TagField):
    widget = TaggitLiveWidget