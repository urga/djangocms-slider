from django.contrib.admin.sites import AdminSite
from django.test import TestCase

# Create your tests here.

from .models import SlideShow, Image
from .admin import ImageAdminInline
from .widgets import AdminImageWidget


class MockRequest(object):
    pass


class MockSuperUser(object):
    def has_perm(self, perm):
        return True


class SlideShowPluginTests(TestCase):
    def setUp(self):
        from .cms_plugins import SlideShowPlugin
        self.plugin = SlideShowPlugin()
        self.site = AdminSite()
        self.request = MockRequest()
        self.request.user = MockSuperUser()

        self.test_slideshow = SlideShow()
        self.test_slideshow.save()

        self.test_image = Image(
            name='bla',
            slideshow_id=self.test_slideshow.pk
        )
        self.test_image.save()

    def test_without_image(self):
        """
        test wether the plugin/model instance is in the context
        and the instance contains no images
        """
        instance = SlideShow()

        rendered_html_dict = self.plugin.render({}, instance, None)

        self.assertIn('instance', rendered_html_dict)
        self.assertEqual(rendered_html_dict['instance'].images.all().count(), 0)

    def test_with_image(self):
        """
        test wether the plugin/model instance is in the context
        and the instance contains the right number of images
        """
        instance = self.test_slideshow
        rendered_html_dict = self.plugin.render({}, instance, None)

        self.assertIn('instance', rendered_html_dict)
        self.assertEqual(rendered_html_dict['instance'].images.all().count(), 1)

    def test_admin(self):
        """
        test if the admin site contains the right fields
        """
        image_admin = ImageAdminInline(SlideShow, self.site)
        self.assertEqual(image_admin.get_fieldsets(self.request),
                         [(None, {'fields': ['slideshow', 'name', 'image']})])
        self.assertEqual(image_admin.get_fieldsets(self.request, self.test_image),
                         [(None, {'fields': ['slideshow', 'name', 'image']})])

    def test_admin_widget(self):
        """
        test if the admin site displays a custom image widget
        """
        image_admin = ImageAdminInline(SlideShow, self.site)
        dbfields = image_admin.model._meta.fields

        for dbfield in dbfields:
            if dbfield.name == 'image':
                self.assertTrue(type(image_admin.formfield_for_dbfield(dbfield).widget) is AdminImageWidget)