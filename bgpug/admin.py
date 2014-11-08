from django.contrib import admin
from django.db import models
from django.forms import Media

from tinymce.widgets import TinyMCE
from zinnia.admin.entry import EntryAdmin as ZinniaEntryAdmin
from zinnia.models.entry import Entry


class EntryAdmin(ZinniaEntryAdmin):
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE},
    }

    def _media(self):
        media = super(EntryAdmin, self).media + Media(
            js=('mce_filebrowser/js/filebrowser_init.js',)
        )
        return media
    media = property(_media)

admin.site.unregister(Entry)
admin.site.register(Entry, EntryAdmin)
