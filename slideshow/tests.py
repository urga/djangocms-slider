from django.contrib.admin.sites import AdminSite
from django.test import TestCase

from .models import SlideShow, Image


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
