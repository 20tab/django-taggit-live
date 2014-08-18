from __future__ import unicode_literals
from django.conf import settings
from django import forms
from django.utils.safestring import mark_safe
from django.core.urlresolvers import reverse
from taggit.forms import TagField
from taggit.utils import edit_string_for_tags


class TaggitLiveWidget(forms.TextInput):

    class Media:
        css = {'all': ('{}taggit_live/css/taggit_live.css'.format(settings.STATIC_URL),)}
        js = ('{}taggit_live/js/taggit_live.js'.format(settings.STATIC_URL),)

    def render(self, name, value, attrs=None):
        if value is not None and not isinstance(value, basestring):
            value = edit_string_for_tags([o.tag for o in value.select_related("tag")])
        rendered = super(TaggitLiveWidget, self).render(name, value, attrs)
        url = reverse("taggit_autocomplete_list")
        js = '<script type="text/javascript">(function($) { $("#%s").taggit_live({callback: "%s"}); })(jQuery || django.jQuery);</script>' % (attrs['id'], url)
        return rendered + mark_safe(js)


class LiveTagField(TagField):
    widget = TaggitLiveWidget