from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _
from adminsortable.admin import SortableAdmin

from .models import SlideShow as SlideShowModel
from .admin import ImageAdminInline as Image


class SlideShowPlugin(CMSPluginBase, SortableAdmin):
    model = SlideShowModel
    name = _('Slideshow')
    render_template = 'slideshow.html'
    inlines = [Image, ]

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context

plugin_pool.register_plugin(SlideShowPlugin)