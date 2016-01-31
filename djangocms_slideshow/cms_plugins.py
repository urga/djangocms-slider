# -*- coding: utf-8 -*-

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _
from .models import SlideShow, Slide


class SlideShowSlidePlugin(CMSPluginBase):
    model = Slide
    module = _("Slideshow")
    name = _("Slide")
    render_template = 'slideshow/slide.html'


class SlideShowPlugin(CMSPluginBase):
    model = SlideShow
    name = _('Slideshow')
    module = _("Slideshow")
    render_template = 'slideshow/slideshow.html'
    allow_children = True
    child_classes = ["SlideShowSlidePlugin"]

    def render(self, context, instance, placeholder):
        context.update({
            'instance': instance,
            'placeholder': placeholder,
        })
        return context

plugin_pool.register_plugin(SlideShowSlidePlugin)
plugin_pool.register_plugin(SlideShowPlugin)
