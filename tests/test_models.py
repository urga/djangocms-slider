from django.test import TestCase

from djangocms_slideshow.models import SlideShow
from djangocms_slideshow.cms_plugins import SlideShowPlugin


class SlideShowPluginTests(TestCase):
    def setUp(self):
        self.plugin = SlideShowPlugin()

    def test_is_plugin_renderable(self):
        """
        test wether the plugin/model instance is in the context
        and the instance contains no images
        """
        instance = SlideShow()

        rendered_html_dict = self.plugin.render({}, instance, None)

        self.assertIn('instance', rendered_html_dict)
