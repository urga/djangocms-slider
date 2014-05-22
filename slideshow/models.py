from cms.models.pluginmodel import CMSPlugin
from django.db import models
from django.utils.translation import ugettext_lazy as _
from adminsortable.models import Sortable

# Create your models here.


class Image(Sortable):
    slideshow = models.ForeignKey('SlideShow', verbose_name=_('Slideshow'), related_name=_('images'))
    name = models.CharField(_('Name'), max_length=255)
    image = models.ImageField(_('Image'), upload_to='slideshow')
    url = models.CharField(_('Url'), max_length=255, blank=True, null=True)

    class Meta(Sortable.Meta):
        verbose_name = _("Image")
        verbose_name_plural = _("Images")
        pass


class SlideShow(CMSPlugin, Sortable):

    def copy_relations(self, old_instance):
        for img in old_instance.images.all():
            img.pk = None
            img.slideshow = self
            img.save()

    class Meta(Sortable.Meta):
        verbose_name = _("Slideshow")
        verbose_name_plural = _("Slideshows")
        pass