# -*- coding: utf-8 -*-

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _
from .models import Slider, Slide


class SlidePlugin(CMSPluginBase):
    model = Slide
    module = _("Slider")
    name = _("Slide")
    render_template = 'djangocms_slider/slide.html'

plugin_pool.register_plugin(SlidePlugin)


class SliderPlugin(CMSPluginBase):
    model = Slider
    name = _('Slider')
    module = _("Slider")
    render_template = 'djangocms_slider/slider.html'
    allow_children = True
    child_classes = ["SlidePlugin"]

    def render(self, context, instance, placeholder):
        context.update({
            'instance': instance,
            'placeholder': placeholder,
        })
        return context


plugin_pool.register_plugin(SliderPlugin)
