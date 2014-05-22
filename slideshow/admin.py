from django.contrib import admin
from adminsortable.admin import SortableAdmin, SortableTabularInline

from .widgets import AdminImageWidget
from .models import SlideShow, Image

# Register your models here.


class ImageAdminInline(SortableTabularInline):
    model = Image

    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == 'image':
            kwargs.pop('request', None)
            kwargs['widget'] = AdminImageWidget
            return db_field.formfield(**kwargs)
        return super(ImageAdminInline, self).formfield_for_dbfield(db_field, **kwargs)


class SlideShowAdmin(SortableAdmin):
    inlines = [ImageAdminInline, ]

admin.site.register(SlideShow, SlideShowAdmin)