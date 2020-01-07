from __future__ import unicode_literals

from django.views import generic


class StaticHtmlView(generic.TemplateView):
    def get_template_names(self):
        return ['static_html/{0}.html'.format(self.kwargs['template_name'])]
