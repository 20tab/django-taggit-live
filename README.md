It's an autocomplete widget for django-taggit TagField:
http://github.com/alex/django-taggit

## Installation

   1. You need to have django-taggit already installed
   2. Clone django-taggit-live
   3. Run setup.py to install taggit_live
   4. Add "taggit_live" to installed apps in your project's settings.
   5. Add the following line to your project's urls.py file:

      (r'', include('taggit_live.urls')),

## Usage


You have to use TaggableManager your models.py file. Example:

``` py
from django.db import models
from taggit.managers import TaggableManager

class SomeModel(models.Model):
        tags = TaggableManager()
```
Then you have to change form field in ModelForm. Example:
``` py
from taggit_live.forms import LiveTagField

class SomeForm(forms.ModelForm):
    tags = LiveTagField()
    class Meta:
        model = SomeModel
```
Finally, you have to include jquery library in your ModelAdmin:
``` py
from taggit_live.forms import LiveTagField

class SomeAdmin(admin.ModelAdmin):
    class Media:
        js = (
            '/path_to/jquery-lib.js',
        )
```
