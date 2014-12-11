from django.conf import settings
from django.conf.urls import (
    include,
    patterns,
    static,
    url,
)
from django.contrib import admin

from bgpug import views

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('zinnia.urls', namespace='zinnia')),
    url(r'^comments/', include('django_comments.urls')),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^mce_filebrowser/', include('mce_filebrowser.urls')),
    url(r'^(?P<template_name>about-us)', views.StaticHtmlView.as_view(), name='about-us')
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^static_html/(?P<template_name>\w+)/$', views.StaticHtmlView.as_view(), name='static-html'),
    )
    urlpatterns += static.static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static.static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
