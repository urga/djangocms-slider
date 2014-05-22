from django.contrib.admin.widgets import AdminFileWidget
from django.utils.translation import ugettext as _
from django.utils.safestring import mark_safe
from easy_thumbnails.files import get_thumbnailer


class AdminImageWidget(AdminFileWidget):

    def render(self, name, value, attrs=None):
        output = []
        if value and getattr(value, 'url', None):
            options = {'size': (140, 140), 'crop': False}
            image_url = value.url
            thumb_url = get_thumbnailer(value).get_thumbnail(options).url
            file_name = str(value)

            output.append(
                u' <a href="%s" target="_blank"><img src="%s" alt="%s" style="height: 100px;" /></a><br /> %s ' %
                (image_url, thumb_url, file_name, _('Change:')))
        output.append(super(AdminFileWidget, self).render(name, value, attrs))
        return mark_safe(u''.join(output))
