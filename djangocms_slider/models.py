import os
from cms.models import CMSPlugin, Page
from cms.utils.compat.dj import python_2_unicode_compatible
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import ugettext_lazy as _

try:
    from cms.models import get_plugin_media_path
except ImportError:
    def get_plugin_media_path(instance, filename):
        """
        See cms.models.pluginmodel.get_plugin_media_path on django CMS 3.0.4+
        for information
        """
        return instance.get_media_path(filename)


@python_2_unicode_compatible
class Slide(CMSPlugin):
    """
    A Slide plugin that contains an image and some text.
    """

    image = models.ImageField(_("image"), upload_to=get_plugin_media_path)
    url = models.CharField(
        _("link"), max_length=255, blank=True, null=True,
        help_text=_("If present, clicking on image will take user to link."))

    page_link = models.ForeignKey(
        Page, verbose_name=_("page"), null=True,
        limit_choices_to={'publisher_is_draft': True}, blank=True,
        help_text=_("If present, clicking on image will take user to "
                    "specified page."))

    caption = models.TextField(
        _("caption"), max_length=255, blank=True, null=True,
        help_text=_("Specifies text that occurs on the slide."))

    def __str__(self):
        if self.caption:
            return self.caption[:40]
        elif self.image:
            # added if, because it raised attribute error when file wasn't
            # defined.
            try:
                return u"%s" % os.path.basename(self.image.name)
            except AttributeError:
                pass
        return u"<empty>"

    def clean(self):
        if self.url and self.page_link:
            raise ValidationError(
                _("You can enter a Link or a Page, but not both."))


@python_2_unicode_compatible
class Slider(CMSPlugin):
    """
    Plugin that can only contain Slides.
    """

    def __str__(self):
        return _(u"%s Images") % self.cmsplugin_set.all().count()
