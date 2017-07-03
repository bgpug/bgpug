from django.conf import settings
from django.conf.urls import (
    include,
    static,
    url,
)
from django.contrib import admin
from django.contrib.sitemaps.views import index, sitemap

from zinnia.sitemaps import EntrySitemap, CategorySitemap

from bgpug import views

admin.autodiscover()

sitemaps = {
    'blog': EntrySitemap,
    'categories': CategorySitemap,
}

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('zinnia.urls', namespace='zinnia')),
    url(r'^comments/', include('django_comments.urls')),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^mce_filebrowser/', include('mce_filebrowser.urls')),
    url(r'^(?P<template_name>about-us)', views.StaticHtmlView.as_view(), name='about-us'),
    url(r'^(?P<template_name>conf2017)', views.StaticHtmlView.as_view(), name='conf2017')
]

urlpatterns += [
    url(r'^sitemap.xml$', index, {'sitemaps': sitemaps}),
    url(r'^sitemap-(?P<section>.+)\.xml$', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]

if settings.DEBUG:
    urlpatterns += [
        url(r'^static_html/(?P<template_name>\w+)/$', views.StaticHtmlView.as_view(), name='static-html'),
    ]
    urlpatterns += static.static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static.static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
